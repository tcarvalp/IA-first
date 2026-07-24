# 📋 Formulário de Assessment — Squad Extrato

Formulário web interativo para coleta de informações nas entrevistas com stakeholders do Assessment do Ciclo de Desenvolvimento de Software.

## 🚀 Como Usar

### Opção 1: Executável (.exe) — sem instalar nada
1. Execute `dist/AssessmentSquadExtrato.exe`
2. Acesse no navegador: **http://localhost:5000**
3. O servidor desliga automaticamente após 30 min de inatividade

### Opção 2: Via Python
```bash
cd formulario-assessment
pip install -r requirements.txt
python app.py
```
Acesse: **http://localhost:5000**

### Acesso de outros computadores na rede
Qualquer pessoa na mesma rede acessa via **http://<SEU_IP>:5000**

## 📂 Estrutura do Projeto

```
formulario-assessment/
├── app.py              # Servidor Flask (aplicação principal)
├── config.py           # Configurações (pasta de salvamento, listas)
├── perguntas.py        # Banco de perguntas (Itens 5, 6 e 7)
├── build_exe.py        # Script para gerar o .exe
├── requirements.txt    # Dependências Python (flask)
├── templates/
│   ├── formulario.html # Interface do formulário com abas
│   └── arquivos.html   # Listagem de arquivos salvos
├── TESTE/
│   ├── test_app.py     # Suite de testes (20 testes)
│   └── relatorio_testes.json
├── dist/
│   └── AssessmentSquadExtrato.exe  # Executável standalone
└── README.md
```

## 🎯 Funcionalidades

- **4 Abas**:
  - 🔍 **5. Qualidade** — 156 perguntas em 18 seções (Engenheiro de Qualidade)
  - 💻 **6. Desenvolvimento** — 57 perguntas em 9 seções (Engenheiro de Desenvolvimento)
  - 🤝 **7. Compartilhado** — 19 perguntas em 4 seções (Ambos)
  - 📝 **Anotações Gerais** — Texto livre para percepções e insights
- **Metadados da entrevista**: Entrevistador, entrevistado, cargo, stakeholder, data
- **Seções em accordion** (recolhidas por padrão, expandem ao clicar)
- **Botão "Não se aplica"** por seção — desativa e marca todas as perguntas como N/A
- **Barra de progresso** por aba (atualiza em tempo real)
- **Barra de salvamento fixa** no rodapé (não ocupa espaço de tela)
- **Salvamento em JSON** na pasta configurável (OneDrive/rede)
- **Alerta ao sair sem salvar**
- **Auto-shutdown** após 30 min de inatividade
- **Listagem de arquivos salvos** em `/arquivos`

## 💾 Salvamento

Os formulários são salvos em JSON na pasta configurada.
Padrão: `~/OneDrive/Assessment_Squad_Extrato/Entrevistas/`

Você pode alterar a pasta diretamente na barra de salvamento no rodapé do formulário.

### Nome do arquivo
```
assessment_{nome_entrevistado}_{timestamp}.json
```

### Estrutura do JSON salvo

```json
{
  "metadata": {
    "entrevistador": "Engenheiro de Qualidade",
    "stakeholder": "Tech Lead / Líder Técnico da Squad",
    "nome_entrevistado": "João Silva",
    "cargo_entrevistado": "Tech Lead",
    "data_entrevista": "2026-07-24",
    "observacoes_gerais": "Entrevista presencial, 1h",
    "data_hora_salvamento": "2026-07-24T14:30:00",
    "versao_formulario": "1.0.0"
  },
  "respostas": {
    "qualidade": { "5.1 Processos de Qualidade | ...": "Resposta..." },
    "desenvolvimento": { "6.1 Arquitetura de Software | ...": "Resposta..." },
    "compartilhadas": { "7.1 Processo de Desenvolvimento | ...": "Resposta..." }
  },
  "anotacoes_gerais_livres": "Percepções e insights adicionais...",
  "estatisticas": {
    "qualidade": { "total": 156, "respondidas": 42 },
    "desenvolvimento": { "total": 57, "respondidas": 30 },
    "compartilhadas": { "total": 19, "respondidas": 15 }
  }
}
```

## 🧪 Testes

Executar a suite completa de 20 testes:
```bash
python TESTE/test_app.py
```

Os testes validam: carregamento de páginas, salvamento de JSONs, metadados, estatísticas, criação de pastas, caracteres especiais, encoding UTF-8, accordions, botão N/A, e mais.

## 🔧 Configuração

Edite `config.py` para alterar:
- `DEFAULT_SAVE_PATH` — Pasta padrão de salvamento
- `ENTREVISTADORES` — Lista de entrevistadores
- `STAKEHOLDERS` — Lista de stakeholders

Edite o topo de `app.py` para alterar:
- `AUTO_SHUTDOWN_MINUTES` — Tempo de inatividade para desligar (padrão: 30 min)

## 📦 Gerar novo .exe

Após qualquer alteração no código:
```bash
python build_exe.py
```
O executável será gerado em `dist/AssessmentSquadExtrato.exe`
