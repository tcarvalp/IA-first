"""
Testes completos do Formulário de Assessment — Squad Extrato

Testa:
1. Carregamento da página principal
2. Carregamento da página de arquivos
3. Salvamento do formulário (todas as abas)
4. Estrutura do JSON salvo
5. Metadados corretos no JSON
6. Respostas organizadas por seção
7. Estatísticas calculadas corretamente
8. Criação automática da pasta de salvamento
9. Botão "Não se aplica" (campos marcados como N/A)
10. Formulário vazio (sem respostas)
11. Caracteres especiais nas respostas
12. Múltiplos salvamentos geram arquivos diferentes
13. Todas as seções de perguntas presentes no formulário
14. Accordion (details/summary) presente no HTML
15. Barra de salvamento fixa no rodapé

Uso: python -m pytest TESTE/test_app.py -v
  ou: python TESTE/test_app.py
"""

import json
import os
import sys
import tempfile
import shutil
from datetime import date

# Adicionar o diretório pai ao path para importar o app
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import app
from config import DEFAULT_SAVE_PATH, ENTREVISTADORES, STAKEHOLDERS
from perguntas import PERGUNTAS_QUALIDADE, PERGUNTAS_DESENVOLVIMENTO, PERGUNTAS_COMPARTILHADAS


class TestConfig:
    """Configuração dos testes."""
    
    def __init__(self):
        self.temp_dir = tempfile.mkdtemp(prefix="assessment_test_")
        self.client = app.test_client()
        app.config["TESTING"] = True

    def cleanup(self):
        if os.path.exists(self.temp_dir):
            shutil.rmtree(self.temp_dir)


def build_form_data(save_path, include_responses=True, mark_na_sections=None):
    """Constrói dados de formulário para testes."""
    data = {
        "entrevistador": ENTREVISTADORES[0],
        "stakeholder": STAKEHOLDERS[0],
        "nome_entrevistado": "João Teste Silva",
        "cargo_entrevistado": "Tech Lead",
        "data_entrevista": str(date.today()),
        "observacoes_gerais": "Entrevista de teste automatizado",
        "save_path": save_path,
    }

    # Preencher respostas de qualidade
    for secao, perguntas in PERGUNTAS_QUALIDADE.items():
        for i, _ in enumerate(perguntas):
            key = f"qual__{secao}__{i}"
            if mark_na_sections and secao in mark_na_sections:
                data[key] = "Não se aplica"
            elif include_responses:
                data[key] = f"Resposta teste qualidade - {secao} - pergunta {i}"
            else:
                data[key] = ""

    # Preencher respostas de desenvolvimento
    for secao, perguntas in PERGUNTAS_DESENVOLVIMENTO.items():
        for i, _ in enumerate(perguntas):
            key = f"dev__{secao}__{i}"
            if include_responses:
                data[key] = f"Resposta teste dev - {secao} - pergunta {i}"
            else:
                data[key] = ""

    # Preencher respostas compartilhadas
    for secao, perguntas in PERGUNTAS_COMPARTILHADAS.items():
        for i, _ in enumerate(perguntas):
            key = f"comp__{secao}__{i}"
            if include_responses:
                data[key] = f"Resposta teste compartilhada - {secao} - pergunta {i}"
            else:
                data[key] = ""

    return data


# =============================================================================
# TESTES
# =============================================================================

def test_01_pagina_principal_carrega(config):
    """Teste 1: A página principal carrega com status 200."""
    response = config.client.get("/")
    assert response.status_code == 200, f"Status esperado 200, recebeu {response.status_code}"
    content = response.data.decode("utf-8")
    assert "Assessment" in content, "Texto 'Assessment' não encontrado na página"
    assert "Squad Extrato" in content, "Texto 'Squad Extrato' não encontrado"
    return True


def test_02_pagina_arquivos_carrega(config):
    """Teste 2: A página de arquivos carrega com status 200."""
    response = config.client.get("/arquivos")
    assert response.status_code == 200, f"Status esperado 200, recebeu {response.status_code}"
    content = response.data.decode("utf-8")
    assert "Arquivos Salvos" in content, "Texto 'Arquivos Salvos' não encontrado"
    return True


def test_03_salvamento_formulario(config):
    """Teste 3: O formulário é salvo corretamente como JSON."""
    data = build_form_data(config.temp_dir)
    response = config.client.post("/salvar", data=data, follow_redirects=True)
    assert response.status_code == 200, f"Status esperado 200, recebeu {response.status_code}"

    # Verificar que o arquivo foi criado
    files = [f for f in os.listdir(config.temp_dir) if f.endswith(".json")]
    assert len(files) >= 1, f"Nenhum arquivo JSON criado na pasta {config.temp_dir}"
    return True


def test_04_estrutura_json(config):
    """Teste 4: O JSON salvo tem a estrutura correta."""
    data = build_form_data(config.temp_dir)
    config.client.post("/salvar", data=data, follow_redirects=True)

    files = sorted([f for f in os.listdir(config.temp_dir) if f.endswith(".json")])
    filepath = os.path.join(config.temp_dir, files[-1])

    with open(filepath, "r", encoding="utf-8") as f:
        doc = json.load(f)

    assert "metadata" in doc, "Chave 'metadata' ausente no JSON"
    assert "respostas" in doc, "Chave 'respostas' ausente no JSON"
    assert "estatisticas" in doc, "Chave 'estatisticas' ausente no JSON"

    assert "qualidade" in doc["respostas"], "Seção 'qualidade' ausente nas respostas"
    assert "desenvolvimento" in doc["respostas"], "Seção 'desenvolvimento' ausente nas respostas"
    assert "compartilhadas" in doc["respostas"], "Seção 'compartilhadas' ausente nas respostas"
    return True


def test_05_metadados_corretos(config):
    """Teste 5: Os metadados são salvos corretamente."""
    data = build_form_data(config.temp_dir)
    config.client.post("/salvar", data=data, follow_redirects=True)

    files = sorted([f for f in os.listdir(config.temp_dir) if f.endswith(".json")])
    filepath = os.path.join(config.temp_dir, files[-1])

    with open(filepath, "r", encoding="utf-8") as f:
        doc = json.load(f)

    meta = doc["metadata"]
    assert meta["entrevistador"] == ENTREVISTADORES[0], "Entrevistador incorreto"
    assert meta["stakeholder"] == STAKEHOLDERS[0], "Stakeholder incorreto"
    assert meta["nome_entrevistado"] == "João Teste Silva", "Nome incorreto"
    assert meta["cargo_entrevistado"] == "Tech Lead", "Cargo incorreto"
    assert meta["data_entrevista"] == str(date.today()), "Data incorreta"
    assert meta["observacoes_gerais"] == "Entrevista de teste automatizado", "Obs incorretas"
    assert "data_hora_salvamento" in meta, "data_hora_salvamento ausente"
    assert meta["versao_formulario"] == "1.0.0", "Versão incorreta"
    return True


def test_06_respostas_organizadas(config):
    """Teste 6: As respostas são organizadas por seção."""
    data = build_form_data(config.temp_dir)
    config.client.post("/salvar", data=data, follow_redirects=True)

    files = sorted([f for f in os.listdir(config.temp_dir) if f.endswith(".json")])
    filepath = os.path.join(config.temp_dir, files[-1])

    with open(filepath, "r", encoding="utf-8") as f:
        doc = json.load(f)

    # Verificar que há respostas em cada seção
    assert len(doc["respostas"]["qualidade"]) > 0, "Nenhuma resposta de qualidade"
    assert len(doc["respostas"]["desenvolvimento"]) > 0, "Nenhuma resposta de desenvolvimento"
    assert len(doc["respostas"]["compartilhadas"]) > 0, "Nenhuma resposta compartilhada"
    return True


def test_07_estatisticas_calculadas(config):
    """Teste 7: As estatísticas são calculadas corretamente."""
    data = build_form_data(config.temp_dir)
    config.client.post("/salvar", data=data, follow_redirects=True)

    files = sorted([f for f in os.listdir(config.temp_dir) if f.endswith(".json")])
    filepath = os.path.join(config.temp_dir, files[-1])

    with open(filepath, "r", encoding="utf-8") as f:
        doc = json.load(f)

    stats = doc["estatisticas"]

    # Total de perguntas esperado
    total_qual = sum(len(v) for v in PERGUNTAS_QUALIDADE.values())
    total_dev = sum(len(v) for v in PERGUNTAS_DESENVOLVIMENTO.values())
    total_comp = sum(len(v) for v in PERGUNTAS_COMPARTILHADAS.values())

    assert stats["qualidade"]["total"] == total_qual, \
        f"Total qualidade: esperado {total_qual}, recebeu {stats['qualidade']['total']}"
    assert stats["desenvolvimento"]["total"] == total_dev, \
        f"Total dev: esperado {total_dev}, recebeu {stats['desenvolvimento']['total']}"
    assert stats["compartilhadas"]["total"] == total_comp, \
        f"Total comp: esperado {total_comp}, recebeu {stats['compartilhadas']['total']}"

    # Com respostas preenchidas, respondidas deve ser > 0
    assert stats["qualidade"]["respondidas"] == total_qual, \
        f"Respondidas qualidade: esperado {total_qual}, recebeu {stats['qualidade']['respondidas']}"
    assert stats["desenvolvimento"]["respondidas"] == total_dev, \
        f"Respondidas dev: esperado {total_dev}, recebeu {stats['desenvolvimento']['respondidas']}"
    assert stats["compartilhadas"]["respondidas"] == total_comp, \
        f"Respondidas comp: esperado {total_comp}, recebeu {stats['compartilhadas']['respondidas']}"
    return True


def test_08_criacao_pasta_automatica(config):
    """Teste 8: A pasta de salvamento é criada automaticamente."""
    nova_pasta = os.path.join(config.temp_dir, "subpasta", "nova")
    assert not os.path.exists(nova_pasta), "Pasta já existe antes do teste"

    data = build_form_data(nova_pasta)
    config.client.post("/salvar", data=data, follow_redirects=True)

    assert os.path.exists(nova_pasta), "Pasta não foi criada automaticamente"
    files = [f for f in os.listdir(nova_pasta) if f.endswith(".json")]
    assert len(files) >= 1, "Arquivo não foi salvo na pasta criada"
    return True


def test_09_nao_se_aplica(config):
    """Teste 9: Campos marcados como 'Não se aplica' são salvos corretamente."""
    secao_na = list(PERGUNTAS_QUALIDADE.keys())[0]  # Primeira seção
    data = build_form_data(config.temp_dir, mark_na_sections=[secao_na])
    config.client.post("/salvar", data=data, follow_redirects=True)

    files = sorted([f for f in os.listdir(config.temp_dir) if f.endswith(".json")])
    filepath = os.path.join(config.temp_dir, files[-1])

    with open(filepath, "r", encoding="utf-8") as f:
        doc = json.load(f)

    # Verificar que as respostas da seção N/A estão como "Não se aplica"
    for chave, valor in doc["respostas"]["qualidade"].items():
        if secao_na.replace(" ", " ") in chave:
            assert valor == "Não se aplica", \
                f"Esperado 'Não se aplica' para '{chave}', recebeu '{valor}'"
    return True


def test_10_formulario_vazio(config):
    """Teste 10: Formulário sem respostas é salvo com campos vazios."""
    data = build_form_data(config.temp_dir, include_responses=False)
    config.client.post("/salvar", data=data, follow_redirects=True)

    files = sorted([f for f in os.listdir(config.temp_dir) if f.endswith(".json")])
    filepath = os.path.join(config.temp_dir, files[-1])

    with open(filepath, "r", encoding="utf-8") as f:
        doc = json.load(f)

    stats = doc["estatisticas"]
    assert stats["qualidade"]["respondidas"] == 0, "Deveria ter 0 respondidas"
    assert stats["desenvolvimento"]["respondidas"] == 0, "Deveria ter 0 respondidas"
    assert stats["compartilhadas"]["respondidas"] == 0, "Deveria ter 0 respondidas"
    return True


def test_11_caracteres_especiais(config):
    """Teste 11: Caracteres especiais são salvos corretamente."""
    data = build_form_data(config.temp_dir)
    # Sobrescrever uma resposta com caracteres especiais
    first_secao = list(PERGUNTAS_QUALIDADE.keys())[0]
    special_text = 'Teste com "aspas", <tags>, acentuação: ção, émojis: 🚀, e backslash: \\'
    data[f"qual__{first_secao}__0"] = special_text

    config.client.post("/salvar", data=data, follow_redirects=True)

    files = sorted([f for f in os.listdir(config.temp_dir) if f.endswith(".json")])
    filepath = os.path.join(config.temp_dir, files[-1])

    with open(filepath, "r", encoding="utf-8") as f:
        doc = json.load(f)

    # Verificar que o texto especial foi salvo
    found = False
    for valor in doc["respostas"]["qualidade"].values():
        if "émojis: 🚀" in valor:
            found = True
            break
    assert found, "Caracteres especiais não foram salvos corretamente"
    return True


def test_12_multiplos_salvamentos(config):
    """Teste 12: Múltiplos salvamentos geram arquivos diferentes."""
    import time

    data = build_form_data(config.temp_dir)
    config.client.post("/salvar", data=data, follow_redirects=True)
    time.sleep(1.1)  # Esperar 1s para timestamp diferente
    config.client.post("/salvar", data=data, follow_redirects=True)

    files = [f for f in os.listdir(config.temp_dir) if f.endswith(".json")]
    assert len(files) >= 2, f"Esperado ao menos 2 arquivos, encontrou {len(files)}"
    return True


def test_13_secoes_presentes_no_html(config):
    """Teste 13: Todas as seções de perguntas estão presentes no HTML."""
    response = config.client.get("/")
    content = response.data.decode("utf-8")

    for secao in PERGUNTAS_QUALIDADE.keys():
        assert secao in content, f"Seção '{secao}' não encontrada no HTML"

    for secao in PERGUNTAS_DESENVOLVIMENTO.keys():
        assert secao in content, f"Seção '{secao}' não encontrada no HTML"

    for secao in PERGUNTAS_COMPARTILHADAS.keys():
        assert secao in content, f"Seção '{secao}' não encontrada no HTML"
    return True


def test_14_accordion_presente(config):
    """Teste 14: Elementos de accordion (details/summary) estão no HTML."""
    response = config.client.get("/")
    content = response.data.decode("utf-8")

    total_secoes = (
        len(PERGUNTAS_QUALIDADE) +
        len(PERGUNTAS_DESENVOLVIMENTO) +
        len(PERGUNTAS_COMPARTILHADAS)
    )

    details_count = content.count("<details")
    assert details_count == total_secoes, \
        f"Esperado {total_secoes} <details>, encontrou {details_count}"

    summary_count = content.count("<summary")
    assert summary_count == total_secoes, \
        f"Esperado {total_secoes} <summary>, encontrou {summary_count}"
    return True


def test_15_barra_salvamento_fixa(config):
    """Teste 15: A barra de salvamento fixa está no HTML."""
    response = config.client.get("/")
    content = response.data.decode("utf-8")

    assert "save-bar" in content, "Classe 'save-bar' não encontrada no HTML"
    assert 'name="save_path"' in content, "Campo save_path não encontrado"
    assert "Salvar Entrevista" in content, "Botão 'Salvar Entrevista' não encontrado"
    return True


def test_16_nome_arquivo_correto(config):
    """Teste 16: O nome do arquivo segue o padrão esperado."""
    data = build_form_data(config.temp_dir)
    config.client.post("/salvar", data=data, follow_redirects=True)

    files = [f for f in os.listdir(config.temp_dir) if f.endswith(".json")]
    assert len(files) >= 1

    # Verificar padrão: assessment_{nome}_{timestamp}.json
    filename = files[0]
    assert filename.startswith("assessment_"), f"Arquivo não começa com 'assessment_': {filename}"
    assert "João_Teste_Silva" in filename, f"Nome do entrevistado não está no arquivo: {filename}"
    assert filename.endswith(".json"), f"Arquivo não termina com .json: {filename}"
    return True


def test_17_botao_nao_se_aplica_no_html(config):
    """Teste 17: O botão 'Não se aplica' está presente em todas as seções."""
    response = config.client.get("/")
    content = response.data.decode("utf-8")

    total_secoes = (
        len(PERGUNTAS_QUALIDADE) +
        len(PERGUNTAS_DESENVOLVIMENTO) +
        len(PERGUNTAS_COMPARTILHADAS)
    )

    btn_count = content.count("btn-na")
    # btn-na aparece no CSS (3x: classe, hover, active) + uma vez por seção
    assert btn_count >= total_secoes, \
        f"Esperado ao menos {total_secoes} referências 'btn-na', encontrou {btn_count}"
    return True


def test_18_entrevistadores_no_formulario(config):
    """Teste 18: Todos os entrevistadores aparecem no formulário."""
    response = config.client.get("/")
    content = response.data.decode("utf-8")

    for entrevistador in ENTREVISTADORES:
        assert entrevistador in content, \
            f"Entrevistador '{entrevistador}' não encontrado no HTML"
    return True


def test_19_stakeholders_no_formulario(config):
    """Teste 19: Todos os stakeholders aparecem no formulário."""
    response = config.client.get("/")
    content = response.data.decode("utf-8")

    for stakeholder in STAKEHOLDERS:
        assert stakeholder in content, \
            f"Stakeholder '{stakeholder}' não encontrado no HTML"
    return True


def test_20_json_utf8_encoding(config):
    """Teste 20: O JSON é salvo em UTF-8 com acentuação correta."""
    data = build_form_data(config.temp_dir)
    first_secao = list(PERGUNTAS_QUALIDADE.keys())[0]
    data[f"qual__{first_secao}__0"] = "Automação de testes com cobertura de código"
    config.client.post("/salvar", data=data, follow_redirects=True)

    files = sorted([f for f in os.listdir(config.temp_dir) if f.endswith(".json")])
    filepath = os.path.join(config.temp_dir, files[-1])

    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    assert "Automação" in content, "Acentuação não foi preservada no arquivo"
    assert "\\u" not in content.split('"Automa')[0][-5:], "JSON está usando escape unicode"
    return True


# =============================================================================
# RUNNER
# =============================================================================

def run_all_tests():
    """Executa todos os testes e gera relatório."""
    config = TestConfig()
    
    tests = [
        test_01_pagina_principal_carrega,
        test_02_pagina_arquivos_carrega,
        test_03_salvamento_formulario,
        test_04_estrutura_json,
        test_05_metadados_corretos,
        test_06_respostas_organizadas,
        test_07_estatisticas_calculadas,
        test_08_criacao_pasta_automatica,
        test_09_nao_se_aplica,
        test_10_formulario_vazio,
        test_11_caracteres_especiais,
        test_12_multiplos_salvamentos,
        test_13_secoes_presentes_no_html,
        test_14_accordion_presente,
        test_15_barra_salvamento_fixa,
        test_16_nome_arquivo_correto,
        test_17_botao_nao_se_aplica_no_html,
        test_18_entrevistadores_no_formulario,
        test_19_stakeholders_no_formulario,
        test_20_json_utf8_encoding,
    ]

    results = []
    passed = 0
    failed = 0

    print("\n" + "=" * 70)
    print("  TESTES DO FORMULÁRIO DE ASSESSMENT — Squad Extrato")
    print("=" * 70 + "\n")

    for test_func in tests:
        # Limpar pasta temp para cada teste (exceto test_12)
        if test_func != test_12_multiplos_salvamentos:
            for f in os.listdir(config.temp_dir):
                fp = os.path.join(config.temp_dir, f)
                if os.path.isfile(fp):
                    os.remove(fp)
                elif os.path.isdir(fp):
                    shutil.rmtree(fp)

        try:
            test_func(config)
            status = "✅ PASSOU"
            passed += 1
            results.append({"teste": test_func.__doc__, "status": "PASSOU", "erro": None})
        except AssertionError as e:
            status = f"❌ FALHOU: {e}"
            failed += 1
            results.append({"teste": test_func.__doc__, "status": "FALHOU", "erro": str(e)})
        except Exception as e:
            status = f"❌ ERRO: {e}"
            failed += 1
            results.append({"teste": test_func.__doc__, "status": "ERRO", "erro": str(e)})

        print(f"  {status}")
        print(f"    {test_func.__doc__}\n")

    # Resumo
    print("=" * 70)
    print(f"  RESULTADO: {passed} passaram, {failed} falharam, {len(tests)} total")
    print("=" * 70 + "\n")

    # Salvar relatório JSON
    report_dir = os.path.dirname(os.path.abspath(__file__))
    report_path = os.path.join(report_dir, "relatorio_testes.json")
    
    report = {
        "resumo": {
            "total": len(tests),
            "passou": passed,
            "falhou": failed,
            "taxa_sucesso": f"{(passed / len(tests)) * 100:.1f}%",
        },
        "testes": results,
    }

    with open(report_path, "w", encoding="utf-8") as f:
        json.dump(report, f, ensure_ascii=False, indent=2)
    
    print(f"  📄 Relatório salvo em: {report_path}\n")

    # Cleanup
    config.cleanup()

    return failed == 0


if __name__ == "__main__":
    success = run_all_tests()
    sys.exit(0 if success else 1)
