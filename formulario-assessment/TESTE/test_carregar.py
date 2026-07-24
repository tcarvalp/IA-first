"""Teste especifico: carregar JSON e salvar alteracoes."""
import sys, os, json, tempfile, shutil
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from app import app

client = app.test_client()
tmp = tempfile.mkdtemp()
print("Pasta temp:", tmp)

# 1. Salvar formulario novo
data = {
    "entrevistador": "Engenheiro de Qualidade",
    "stakeholder": "Tech Lead",
    "nome_entrevistado": "Teste",
    "cargo_entrevistado": "Dev",
    "data_entrevista": "2026-07-24",
    "observacoes_gerais": "",
    "save_path": tmp,
    "qual__5.1 Processos de Qualidade__0": "Resposta Original",
}
r = client.post("/salvar", data=data, follow_redirects=False)
print(f"1. Salvar novo - status: {r.status_code}")

files = [f for f in os.listdir(tmp) if f.endswith(".json")]
print(f"   Arquivo criado: {files[0]}")

with open(os.path.join(tmp, files[0]), "r", encoding="utf-8") as f:
    doc = json.load(f)
first_val = list(doc["respostas"]["qualidade"].values())[0]
print(f"   Resposta salva: {first_val}")
assert first_val == "Resposta Original", "FALHA: resposta original nao salva"

# 2. Carregar o arquivo
r = client.get(f"/carregar/{files[0]}?path={tmp}")
print(f"2. Carregar - status: {r.status_code}")
html = r.data.decode()
has_hidden = 'name="loaded_file"' in html
has_filename = files[0] in html
print(f"   Hidden loaded_file presente: {has_hidden}")
print(f"   Filename no hidden: {has_filename}")
assert has_hidden, "FALHA: campo hidden loaded_file ausente"
assert has_filename, "FALHA: nome do arquivo nao esta no hidden"

# 3. Salvar com alteracao
data2 = {
    "entrevistador": "Engenheiro de Qualidade",
    "stakeholder": "Tech Lead",
    "nome_entrevistado": "Teste",
    "cargo_entrevistado": "Dev",
    "data_entrevista": "2026-07-24",
    "observacoes_gerais": "",
    "save_path": tmp,
    "loaded_file": files[0],
    "qual__5.1 Processos de Qualidade__0": "Resposta ALTERADA",
}
r = client.post("/salvar", data=data2, follow_redirects=False)
print(f"3. Salvar alteracao - status: {r.status_code}")

files_after = [f for f in os.listdir(tmp) if f.endswith(".json")]
print(f"   Qtd arquivos: {len(files_after)}")
print(f"   Mesmo arquivo: {files_after[0] == files[0]}")

with open(os.path.join(tmp, files[0]), "r", encoding="utf-8") as f:
    doc2 = json.load(f)
new_val = list(doc2["respostas"]["qualidade"].values())[0]
print(f"   Resposta agora: {new_val}")
assert new_val == "Resposta ALTERADA", f"FALHA: esperado 'Resposta ALTERADA', recebeu '{new_val}'"

print("\n=== TODOS OS TESTES PASSARAM ===")
shutil.rmtree(tmp)
