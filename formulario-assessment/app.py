"""
Formulário de Assessment — Squad Extrato
Ciclo de Desenvolvimento de Software

Uso: python app.py
Acesso: http://localhost:5000
"""

import json
import os
import sys
import threading
import time
from datetime import datetime

from flask import Flask, render_template, request, redirect, url_for, flash


# Auto-shutdown: desliga o servidor se ninguém acessar por N minutos
AUTO_SHUTDOWN_MINUTES = 30
last_activity = time.time()


def auto_shutdown_watcher():
    """Thread que monitora inatividade e desliga o servidor."""
    global last_activity
    while True:
        time.sleep(60)  # Verifica a cada 1 minuto
        idle_minutes = (time.time() - last_activity) / 60
        if idle_minutes >= AUTO_SHUTDOWN_MINUTES:
            print(f"\n⏱️  Servidor inativo por {AUTO_SHUTDOWN_MINUTES} min. Desligando...")
            os._exit(0)


def get_base_path():
    """Retorna o diretório base, compatível com PyInstaller."""
    if getattr(sys, 'frozen', False):
        return sys._MEIPASS
    return os.path.dirname(os.path.abspath(__file__))


base_path = get_base_path()

# Importar config e perguntas (compatível com PyInstaller)
sys.path.insert(0, base_path)
from config import DEFAULT_SAVE_PATH, ENTREVISTADORES, STAKEHOLDERS
from perguntas import PERGUNTAS_QUALIDADE, PERGUNTAS_DESENVOLVIMENTO, PERGUNTAS_COMPARTILHADAS

app = Flask(__name__, template_folder=os.path.join(base_path, "templates"))
app.secret_key = "assessment-squad-extrato-2026"
app.config["TEMPLATES_AUTO_RELOAD"] = True
app.jinja_env.auto_reload = True


@app.before_request
def update_activity():
    """Atualiza timestamp de última atividade a cada request."""
    global last_activity
    last_activity = time.time()


@app.after_request
def no_cache(response):
    """Impede cache do navegador para garantir formulário limpo após salvar."""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Pragma"] = "no-cache"
    response.headers["Expires"] = "0"
    return response


@app.route("/")
def index():
    """Página principal com o formulário."""
    # Verificar se há dados pré-carregados de um arquivo
    loaded_data = None
    loaded_file = request.args.get("loaded_file", "")
    
    return render_template(
        "formulario.html",
        entrevistadores=ENTREVISTADORES,
        stakeholders=STAKEHOLDERS,
        perguntas_qualidade=PERGUNTAS_QUALIDADE,
        perguntas_desenvolvimento=PERGUNTAS_DESENVOLVIMENTO,
        perguntas_compartilhadas=PERGUNTAS_COMPARTILHADAS,
        save_path=DEFAULT_SAVE_PATH,
        loaded_data=loaded_data,
        loaded_file=loaded_file,
    )


@app.route("/carregar/<filename>")
def carregar(filename):
    """Carrega um JSON salvo e renderiza o formulário preenchido."""
    save_path = request.args.get("path", DEFAULT_SAVE_PATH)
    filepath = os.path.join(save_path, filename)

    if not os.path.exists(filepath):
        flash(f"Arquivo não encontrado: {filename}", "error")
        return redirect(url_for("index"))

    try:
        with open(filepath, "r", encoding="utf-8") as f:
            loaded_data = json.load(f)
    except (json.JSONDecodeError, OSError) as e:
        flash(f"Erro ao ler arquivo: {e}", "error")
        return redirect(url_for("index"))

    return render_template(
        "formulario.html",
        entrevistadores=ENTREVISTADORES,
        stakeholders=STAKEHOLDERS,
        perguntas_qualidade=PERGUNTAS_QUALIDADE,
        perguntas_desenvolvimento=PERGUNTAS_DESENVOLVIMENTO,
        perguntas_compartilhadas=PERGUNTAS_COMPARTILHADAS,
        save_path=save_path,
        loaded_data=loaded_data,
        loaded_file=filename,
    )


@app.route("/salvar", methods=["POST"])
def salvar():
    """Salva o formulário como JSON."""
    form_data = request.form

    # Metadados
    metadados = {
        "entrevistador": form_data.get("entrevistador", ""),
        "stakeholder": form_data.get("stakeholder", ""),
        "nome_entrevistado": form_data.get("nome_entrevistado", ""),
        "cargo_entrevistado": form_data.get("cargo_entrevistado", ""),
        "data_entrevista": form_data.get("data_entrevista", ""),
        "observacoes_gerais": form_data.get("observacoes_gerais", ""),
        "data_hora_salvamento": datetime.now().isoformat(),
        "versao_formulario": "1.0.0",
    }

    # Pasta de salvamento
    save_path = form_data.get("save_path", DEFAULT_SAVE_PATH).strip()
    if not save_path:
        save_path = DEFAULT_SAVE_PATH

    # Coletar respostas organizadas por seção
    respostas_qualidade = {}
    respostas_desenvolvimento = {}
    respostas_compartilhadas = {}

    for key, value in form_data.items():
        if key.startswith("qual__"):
            campo = key.replace("qual__", "").replace("__", " | ", 1).replace("__", " ")
            respostas_qualidade[campo] = value.strip()
        elif key.startswith("dev__"):
            campo = key.replace("dev__", "").replace("__", " | ", 1).replace("__", " ")
            respostas_desenvolvimento[campo] = value.strip()
        elif key.startswith("comp__"):
            campo = key.replace("comp__", "").replace("__", " | ", 1).replace("__", " ")
            respostas_compartilhadas[campo] = value.strip()

    # Montar documento
    documento = {
        "metadata": metadados,
        "respostas": {
            "qualidade": respostas_qualidade,
            "desenvolvimento": respostas_desenvolvimento,
            "compartilhadas": respostas_compartilhadas,
        },
        "anotacoes_gerais_livres": form_data.get("anotacoes_gerais_livres", "").strip(),
        "estatisticas": {
            "qualidade": {
                "total": len(respostas_qualidade),
                "respondidas": sum(1 for v in respostas_qualidade.values() if v),
            },
            "desenvolvimento": {
                "total": len(respostas_desenvolvimento),
                "respondidas": sum(1 for v in respostas_desenvolvimento.values() if v),
            },
            "compartilhadas": {
                "total": len(respostas_compartilhadas),
                "respondidas": sum(1 for v in respostas_compartilhadas.values() if v),
            },
        },
    }

    # Criar pasta e salvar
    try:
        os.makedirs(save_path, exist_ok=True)
    except OSError as e:
        flash(f"Erro ao criar pasta: {e}", "error")
        return redirect(url_for("index"))

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    nome_clean = metadados["nome_entrevistado"].replace(" ", "_") or "sem_nome"

    # Se está editando um arquivo carregado, sobrescrever o mesmo arquivo
    loaded_file = form_data.get("loaded_file", "").strip()
    if loaded_file:
        nome_arquivo = loaded_file
    else:
        nome_arquivo = f"assessment_{nome_clean}_{timestamp}.json"

    filepath = os.path.join(save_path, nome_arquivo)

    try:
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(documento, f, ensure_ascii=False, indent=2)
        flash(f"Formulário salvo com sucesso: {filepath}", "success")
    except OSError as e:
        flash(f"Erro ao salvar: {e}", "error")

    return redirect(url_for("index"))


@app.route("/arquivos")
def listar_arquivos():
    """Lista os arquivos JSON salvos."""
    save_path = request.args.get("path", DEFAULT_SAVE_PATH)
    arquivos = []

    if os.path.exists(save_path):
        for f in sorted(os.listdir(save_path), reverse=True):
            if f.endswith(".json"):
                filepath = os.path.join(save_path, f)
                size = os.path.getsize(filepath)
                mod_time = datetime.fromtimestamp(os.path.getmtime(filepath))
                arquivos.append({
                    "nome": f,
                    "tamanho_kb": round(size / 1024, 1),
                    "modificado": mod_time.strftime("%d/%m/%Y %H:%M"),
                })

    return render_template("arquivos.html", arquivos=arquivos, save_path=save_path)


if __name__ == "__main__":
    print("\n" + "=" * 60)
    print("  📋 Formulário de Assessment — Squad Extrato")
    print("  🌐 Acesse: http://localhost:5000")
    print("  📂 Salvando em:", DEFAULT_SAVE_PATH)
    print(f"  ⏱️  Auto-desliga após {AUTO_SHUTDOWN_MINUTES} min de inatividade")
    print("=" * 60 + "\n")

    # Iniciar thread de auto-shutdown
    watcher = threading.Thread(target=auto_shutdown_watcher, daemon=True)
    watcher.start()

    # Para acesso na rede, use host='0.0.0.0'
    app.run(debug=False, host="0.0.0.0", port=5000)
