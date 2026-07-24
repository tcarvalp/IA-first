# 📋 Formulário de Assessment — Squad Extrato

Formulário web interativo para coleta de informações nas entrevistas com stakeholders do Assessment do Ciclo de Desenvolvimento de Software.

## 🚀 Como Usar

### Pré-requisitos
- Python 3.8+ instalado

### Instalação (uma única vez)

```bash
cd formulario-assessment
pip install -r requirements.txt
```

### Executar

```bash
python app.py
```

Acesse no navegador: **http://localhost:5000**

Para acesso de outros computadores na rede: **http://<SEU_IP>:5000**

## 📂 Estrutura

```
formulario-assessment/
├── app.py              # Servidor Flask (aplicação principal)
├── config.py           # Configurações (pasta de salvamento, listas)
├── perguntas.py        # Banco de perguntas (Itens 5, 6 e 7)
├── requirements.txt    # Dependências Python
├── templates/
│   ├── formulario.html # Interface do formulário com abas
│   └── arquivos.html   # Listagem de arquivos salvos
└── README.md
```

## 🎯 Funcionalidades

- **3 Abas**: Qualidade (Item 5), Desenvolvimento (Item 6), Compartilhado (Item 7)
- **Metadados completos**: Entrevistador, entrevistado, cargo, stakeholder, data
- **Campo de texto livre** para cada pergunta
- **Barra de progresso** por aba (atualiza em tempo real)
- **Salvamento em JSON** na pasta configurável (OneDrive/rede)
- **Alerta ao sair sem salvar**
- **Listagem de entrevistas já salvas**

## 💾 Salvamento

Os formulários são salvos em JSON na pasta configurada.
Padrão: `~/OneDrive/Assessment_Squad_Extrato/Entrevistas/`

Você pode alterar a pasta diretamente no formulário antes de salvar.

### Nome do arquivo
```
assessment_{nome_entrevistado}_{timestamp}.json
```

### Estrutura do JSON

```json
{
  "metadata": {
    "entrevistador": "Engenheiro de Qualidade",
    "stakeholder": "Tech Lead / Líder Técnico da Squad",
    "nome_entrevistado": "João Silva",
    "cargo_entrevistado": "Tech Lead",
    "data_entrevista": "2026-07-23",
    "observacoes_gerais": "Entrevista presencial, 1h",
    "data_hora_salvamento": "2026-07-23T14:30:00",
    "versao_formulario": "1.0.0"
  },
  "respostas": {
    "qualidade": { ... },
    "desenvolvimento": { ... },
    "compartilhadas": { ... }
  },
  "estatisticas": {
    "qualidade": { "total": 150, "respondidas": 42 },
    "desenvolvimento": { "total": 55, "respondidas": 30 },
    "compartilhadas": { "total": 19, "respondidas": 15 }
  }
}
```

## 🌐 Acesso por Múltiplas Pessoas

### Opção 1: Cada um roda local (mais simples)
Cada analista executa `python app.py` na sua máquina.
Os JSONs vão para a pasta do OneDrive compartilhada.

### Opção 2: Servidor na rede (recomendado)
Rode numa máquina acessível na rede:
```bash
python app.py
```
O app já escuta em `0.0.0.0:5000` — colegas acessam via `http://<IP_DA_MAQUINA>:5000`

### Opção 3: Deploy gratuito (Render, Railway, PythonAnywhere)
Suba o código num repo GitHub e faça deploy em:
- [Render](https://render.com) — gratuito
- [Railway](https://railway.app) — gratuito até certo uso
- [PythonAnywhere](https://www.pythonanywhere.com) — gratuito

> ⚠️ No deploy em nuvem, o salvamento em pasta local não funciona.
> Nesse caso, seria necessário integrar com banco de dados ou storage.

## 🔧 Configuração

Edite `config.py` para alterar:
- `DEFAULT_SAVE_PATH` — Pasta padrão de salvamento
- `ENTREVISTADORES` — Lista de entrevistadores
- `STAKEHOLDERS` — Lista de stakeholders
