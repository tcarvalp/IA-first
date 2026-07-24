# Configuração do formulário de Assessment
# Altere o caminho abaixo para a pasta do OneDrive onde deseja salvar os formulários

import os

# Pasta padrão para salvar os JSONs (altere para seu caminho do OneDrive)
DEFAULT_SAVE_PATH = os.path.join(
    os.path.expanduser("~"),
    "OneDrive",
    "Assessment_Squad_Extrato",
    "Entrevistas"
)

# Opções de entrevistador
ENTREVISTADORES = [
    "Engenheiro de Qualidade",
    "Engenheiro de Desenvolvimento",
    "Engenheiro de Qualidade + Engenheiro de Desenvolvimento (Ambos)"
]

# Stakeholders disponíveis para entrevista
STAKEHOLDERS = [
    "Tech Lead / Líder Técnico da Squad",
    "Product Owner (PO)",
    "Scrum Master / Agile Coach",
    "Desenvolvedores Mobile (iOS/Android)",
    "Desenvolvedores Backend/APIs",
    "Desenvolvedores Frontend Web",
    "QA / Analistas de Teste da Squad",
    "DevOps / SRE",
    "Arquiteto de Soluções",
    "UX/UI Designer",
    "Segurança da Informação (AppSec)",
    "Gestor da área / Coordenação",
    "Outro"
]
