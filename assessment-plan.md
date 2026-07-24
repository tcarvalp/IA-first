# Assessment do Ciclo de Desenvolvimento de Software
## Squad Extrato - APP BancÃ¡rio (Mobile + Portal Web)

---

## 1. Objetivo

Mapear o estado atual (AS IS) e desenhar o estado desejado (TO BE) do ciclo de desenvolvimento de software da Squad Extrato, cobrindo documentaÃ§Ã£o, processos, arquitetura, tecnologias, qualidade e entrega.

---

## 2. Escopo

- Funcionalidades de extrato no APP mobile do banco
- Portal web do banco (em desenho/evoluÃ§Ã£o)
- Todo o ciclo de vida do software: ideaÃ§Ã£o â†’ desenvolvimento â†’ testes â†’ deploy â†’ monitoramento

---

## 3. DivisÃ£o de Responsabilidades

| Ãrea | ResponsÃ¡vel |
|------|-------------|
| Qualidade, Testes, Processos de QA, MÃ©tricas de Defeitos | Engenheiro de Qualidade (Engenheiro de Qualidade) |
| Desenvolvimento, Arquitetura, DevOps, CÃ³digo, Frameworks | Engenheiro de Desenvolvimento (Engenheiro de Desenvolvimento) |

---

## 4. Stakeholders a Entrevistar

| Pessoa/Papel | TÃ³picos | Quem entrevista |
|--------------|---------|-----------------|
| Tech Lead / LÃ­der TÃ©cnico da Squad | Arquitetura, decisÃµes tÃ©cnicas, dÃ©bitos tÃ©cnicos, roadmap | Engenheiro de Desenvolvimento |
| Product Owner (PO) | Backlog, priorizaÃ§Ã£o, requisitos, fluxo de demandas | Engenheiro de Qualidade + Engenheiro de Desenvolvimento |
| Scrum Master / Agile Coach | CerimÃ´nias, mÃ©tricas de fluxo, impedimentos recorrentes | Engenheiro de Qualidade + Engenheiro de Desenvolvimento |
| Desenvolvedores Mobile (iOS/Android) | Stack, padrÃµes, code review, CI/CD, testes unitÃ¡rios | Engenheiro de Desenvolvimento |
| Desenvolvedores Backend/APIs | Stack, contratos de API, integraÃ§Ãµes, observabilidade | Engenheiro de Desenvolvimento |
| Desenvolvedores Frontend Web | Stack web, design system, acessibilidade | Engenheiro de Desenvolvimento |
| QA / Analistas de Teste da Squad | EstratÃ©gia de testes, automaÃ§Ã£o, ambientes, cobertura | Engenheiro de Qualidade |
| DevOps / SRE | Pipelines, infra, deploys, rollback, monitoramento | Engenheiro de Desenvolvimento |
| Arquiteto de SoluÃ§Ãµes (se existir) | VisÃ£o macro, integraÃ§Ãµes entre sistemas, conformidade | Engenheiro de Desenvolvimento |
| UX/UI Designer | Fluxo de entrega de design, handoff, design system | Engenheiro de Qualidade + Engenheiro de Desenvolvimento |
| SeguranÃ§a da InformaÃ§Ã£o (AppSec) | SAST/DAST, polÃ­ticas de seguranÃ§a, compliance | Engenheiro de Qualidade + Engenheiro de Desenvolvimento |
| Gestor da Ã¡rea / CoordenaÃ§Ã£o | Expectativas, metas, dores estratÃ©gicas | Engenheiro de Qualidade + Engenheiro de Desenvolvimento |

---

## 5. Itens a Levantar â€” Engenheiro de Qualidade (Engenheiro de Qualidade)

### 5.1 Processos de Qualidade

- [ ] Existe estratÃ©gia de teste documentada?
- [ ] Quais tipos de teste sÃ£o executados? (unitÃ¡rio, integraÃ§Ã£o, E2E, regressÃ£o, performance, seguranÃ§a, acessibilidade)
- [ ] Qual a cobertura de testes automatizados atual?
- [ ] Existe pirÃ¢mide de testes definida?
- [ ] Como Ã© feita a gestÃ£o de defeitos? (ferramenta, fluxo, SLA)
- [ ] Existe processo de teste exploratÃ³rio?
- [ ] Como sÃ£o tratados os bugs em produÃ§Ã£o? (hotfix, rollback, comunicaÃ§Ã£o)
- [ ] Existe classificaÃ§Ã£o de defeitos por severidade e prioridade? (matriz severidade Ã— prioridade)
- [ ] Como Ã© definida a severidade de um defeito? (impacto no negÃ³cio, no cliente, financeiro)
- [ ] Ã‰ realizada anÃ¡lise de causa raiz (RCA â€” Root Cause Analysis) para defeitos crÃ­ticos?
- [ ] Existe anÃ¡lise de reincidÃªncia de defeitos? (defeitos recorrentes, mesmo mÃ³dulo/causa)
- [ ] Como os aprendizados dos RCAs realimentam a prevenÃ§Ã£o? (aÃ§Ãµes corretivas, testes adicionais)

### 5.2 AutomaÃ§Ã£o de Testes

- [ ] Quais frameworks de automaÃ§Ã£o sÃ£o utilizados? (mobile, API, web)
- [ ] Existe automaÃ§Ã£o de testes de regressÃ£o?
- [ ] Qual a frequÃªncia de execuÃ§Ã£o dos testes automatizados?
- [ ] Os testes estÃ£o integrados ao pipeline de CI/CD?
- [ ] Existe teste de contrato (contract testing) para APIs?
- [ ] Ferramentas utilizadas (Appium, Detox, Cypress, Selenium, Postman, K6, JMeter, etc.)
- [ ] Existe controle de testes instÃ¡veis (flaky tests)? Como sÃ£o identificados e tratados?
- [ ] Existe processo de quarentena para testes instÃ¡veis?
- [ ] Qual o tempo de execuÃ§Ã£o da suÃ­te automatizada? (Ã© aceitÃ¡vel para o ciclo de entrega?)
- [ ] Qual a confiabilidade da suÃ­te? (taxa de falsos positivos/negativos)
- [ ] Qual o custo/esforÃ§o de manutenÃ§Ã£o da automaÃ§Ã£o? (frequÃªncia de quebras, refatoraÃ§Ãµes)
- [ ] Existe estratÃ©gia para manter a saÃºde da suÃ­te ao longo do tempo? (revisÃ£o, deprecaÃ§Ã£o de testes obsoletos)

### 5.3 Ambientes de Teste

- [ ] Quantos ambientes existem? (dev, QA, staging, homologaÃ§Ã£o, produÃ§Ã£o)
- [ ] Como Ã© feita a gestÃ£o de dados de teste?
- [ ] Existe massa de dados anonimizada/sintÃ©tica?
- [ ] Os ambientes sÃ£o estÃ¡veis e representativos de produÃ§Ã£o?
- [ ] Existe ambiente de performance isolado?

### 5.4 MÃ©tricas de Qualidade

- [ ] Quais mÃ©tricas sÃ£o acompanhadas? (taxa de defeitos, escape rate, MTTR, cobertura, etc.)
- [ ] Existe dashboard de qualidade?
- [ ] Qual o histÃ³rico de incidentes em produÃ§Ã£o nos Ãºltimos 6 meses?
- [ ] Qual o lead time de correÃ§Ã£o de bugs?
- [ ] Existem quality gates objetivos definidos? (critÃ©rios de bloqueio de release)
- [ ] Quais critÃ©rios bloqueiam um release? (cobertura mÃ­nima, zero defeitos crÃ­ticos/bloqueantes, testes verdes)
- [ ] Os quality gates estÃ£o automatizados no pipeline ou sÃ£o verificados manualmente?
- [ ] Existem valores-alvo (targets) definidos para as mÃ©tricas no TO BE? (ex.: cobertura â‰¥ 80%, escape rate < X%, MTTR < Y)
- [ ] Como os targets sÃ£o acompanhados e revisados ao longo do tempo?

### 5.5 Processos e DocumentaÃ§Ã£o

- [ ] Existe Definition of Ready (DoR) e Definition of Done (DoD)?
- [ ] Os critÃ©rios de aceite sÃ£o claros nas histÃ³rias?
- [ ] Existe processo de review de qualidade antes do deploy?
- [ ] Como funciona o processo de homologaÃ§Ã£o com o PO/negÃ³cio?
- [ ] Existe documentaÃ§Ã£o de cenÃ¡rios de teste (casos de teste, BDD, etc.)?
- [ ] Onde fica a documentaÃ§Ã£o? (Confluence, Notion, Wiki, repositÃ³rio)
- [ ] Existe processo formal de UAT / homologaÃ§Ã£o com o negÃ³cio?
- [ ] Quem homologa as entregas? (PO, negÃ³cio, key users)
- [ ] Os critÃ©rios de aceite formais estÃ£o definidos e acordados antes da homologaÃ§Ã£o?
- [ ] Existe registro formal de sign-off da homologaÃ§Ã£o? (evidÃªncia de aprovaÃ§Ã£o)
- [ ] Como Ã© feita a gestÃ£o do ambiente de homologaÃ§Ã£o com o negÃ³cio? (acesso, massa, disponibilidade)
- [ ] Existe SLA/prazo definido para o ciclo de homologaÃ§Ã£o?

### 5.6 Compliance e RegulatÃ³rio

- [ ] Existem testes especÃ­ficos para requisitos regulatÃ³rios (BACEN, LGPD)?
- [ ] Como Ã© garantida a conformidade com normas de seguranÃ§a?
- [ ] Existe auditoria de testes / evidÃªncias de execuÃ§Ã£o?
- [ ] Existem testes especÃ­ficos para requisitos de Open Finance / Open Banking?
- [ ] Como Ã© validada a conformidade no compartilhamento de dados de extrato? (consentimento, escopo, prazo)
- [ ] Existem testes de consentimento e revogaÃ§Ã£o de compartilhamento de dados?
- [ ] Os dados compartilhados via Open Finance sÃ£o consistentes com o extrato exibido nos canais prÃ³prios?
- [ ] Existem testes de conformidade com os padrÃµes e APIs do Open Finance Brasil?

### 5.7 Testes NÃ£o Funcionais â€” Performance

- [ ] Existe estratÃ©gia de testes de performance documentada?
- [ ] Quais tipos de teste de performance sÃ£o executados? (carga, estresse, pico, endurance/soak, escalabilidade)
- [ ] Quais ferramentas sÃ£o utilizadas? (JMeter, Gatling, K6, Locust, Artillery, NeoLoad)
- [ ] Existe baseline de performance definida? (tempo de resposta aceitÃ¡vel para o extrato, throughput mÃ­nimo)
- [ ] Os testes de performance sÃ£o executados em ambiente dedicado ou compartilhado?
- [ ] Existe monitoramento de performance no mobile? (tempo de renderizaÃ§Ã£o, consumo de memÃ³ria, CPU, bateria)
- [ ] Como sÃ£o definidos os SLAs de performance para o extrato? (ex.: carregamento em < 2s no P95)
- [ ] Existe teste de performance integrado ao pipeline de CI/CD?
- [ ] SÃ£o realizados testes de capacidade antes de grandes releases ou campanhas?
- [ ] Existe anÃ¡lise de degradaÃ§Ã£o de performance entre versÃµes?

### 5.8 Testes NÃ£o Funcionais â€” Data Test (Qualidade de Dados)

- [ ] Existe estratÃ©gia de validaÃ§Ã£o/qualidade de dados?
- [ ] Como Ã© garantida a integridade dos dados do extrato? (consistÃªncia entre core banking e APP)
- [ ] Existem testes de validaÃ§Ã£o de dados ponta a ponta? (origem â†’ API â†’ apresentaÃ§Ã£o no APP)
- [ ] Existe monitoramento de data quality em produÃ§Ã£o? (dados ausentes, duplicados, inconsistentes)
- [ ] Como Ã© validada a precisÃ£o dos valores monetÃ¡rios no extrato? (casas decimais, arredondamento, moeda)
- [ ] Existem testes de migraÃ§Ã£o de dados?
- [ ] Existe validaÃ§Ã£o de dados em cenÃ¡rios de alta volumetria? (contas com milhares de transaÃ§Ãµes)
- [ ] Como Ã© tratada a paginaÃ§Ã£o e lazy loading no extrato com grandes volumes?
- [ ] Existe teste de reconciliaÃ§Ã£o entre dados exibidos no APP vs. portal web vs. core banking?
- [ ] Como Ã© garantida a conformidade LGPD nos dados de teste? (anonimizaÃ§Ã£o, mascaramento)

### 5.9 Testes NÃ£o Funcionais â€” SeguranÃ§a

- [ ] Existem testes de seguranÃ§a especÃ­ficos para o APP mobile? (OWASP Mobile Top 10)
- [ ] Ã‰ realizado pentest periÃ³dico na funcionalidade de extrato?
- [ ] Existem testes de autenticaÃ§Ã£o e autorizaÃ§Ã£o? (token expirado, session hijacking, privilege escalation)
- [ ] SÃ£o testados cenÃ¡rios de vazamento de dados sensÃ­veis? (logs, cache, screenshots do extrato)
- [ ] Existe validaÃ§Ã£o de criptografia em trÃ¢nsito e em repouso?
- [ ] Testes de certificate pinning sÃ£o realizados?
- [ ] Como Ã© testada a proteÃ§Ã£o contra scraping/automaÃ§Ã£o maliciosa no extrato?

### 5.10 Testes NÃ£o Funcionais â€” Acessibilidade

- [ ] Existe estratÃ©gia de testes de acessibilidade?
- [ ] Quais guidelines sÃ£o seguidos? (WCAG 2.1, diretrizes de acessibilidade iOS/Android)
- [ ] SÃ£o realizados testes com leitores de tela? (VoiceOver, TalkBack)
- [ ] Existe validaÃ§Ã£o de contraste, tamanhos de fonte e Ã¡reas de toque?
- [ ] A funcionalidade de extrato Ã© navegÃ¡vel via teclado / controles alternativos?
- [ ] Existe automaÃ§Ã£o de testes de acessibilidade? (axe, Accessibility Scanner)

### 5.11 Testes NÃ£o Funcionais â€” Usabilidade e Compatibilidade

- [ ] Existe matrix de dispositivos/OS suportados para testes?
- [ ] SÃ£o realizados testes em dispositivos reais ou apenas emuladores?
- [ ] Existe device farm? (BrowserStack, AWS Device Farm, Samsung Remote Test Lab)
- [ ] Como Ã© testada a compatibilidade com diferentes resoluÃ§Ãµes e tamanhos de tela?
- [ ] SÃ£o realizados testes de comportamento offline / conectividade intermitente?
- [ ] Existe teste de instalaÃ§Ã£o, atualizaÃ§Ã£o e migraÃ§Ã£o de versÃ£o do APP?
- [ ] SÃ£o testados cenÃ¡rios de interrupÃ§Ã£o? (chamada telefÃ´nica, notificaÃ§Ã£o, multitasking)

### 5.12 Testes NÃ£o Funcionais â€” Confiabilidade e ResiliÃªncia

- [ ] Existem testes de resiliÃªncia / chaos engineering?
- [ ] SÃ£o testados cenÃ¡rios de falha de dependÃªncias? (API indisponÃ­vel, timeout, core banking fora)
- [ ] Como Ã© validado o comportamento do APP em cenÃ¡rios de erro? (mensagens amigÃ¡veis, retry, fallback)
- [ ] Existe teste de recuperaÃ§Ã£o apÃ³s falhas? (crash recovery, persistÃªncia de estado)
- [ ] SÃ£o realizados testes de concorrÃªncia? (mÃºltiplas sessÃµes, race conditions)
- [ ] Existe SLA de disponibilidade definido e testado para o extrato?

### 5.13 Testes NÃ£o Funcionais â€” Observabilidade e Monitoramento (visÃ£o QA)

- [ ] QA valida que os logs e traces estÃ£o sendo gerados corretamente?
- [ ] Existe teste de alertas? (o alerta dispara corretamente quando o SLO Ã© violado?)
- [ ] QA participa da definiÃ§Ã£o de SLIs/SLOs?
- [ ] Existem testes de synthetic monitoring para o extrato?
- [ ] Como QA monitora a saÃºde da feature em produÃ§Ã£o pÃ³s-deploy?
- [ ] QA acompanha mÃ©tricas e alertas nas primeiras horas apÃ³s o release? (monitoramento pÃ³s-release ativo)
- [ ] Existem critÃ©rios objetivos para abortar/reverter um release com base em observabilidade?

### 5.14 Processo de Desenvolvimento (visÃ£o QA)

- [ ] Em que momento QA entra no ciclo? (shift-left?)
- [ ] QA participa do refinamento e planning?
- [ ] Existe pair testing ou mob testing?
- [ ] Como Ã© o handoff dev â†’ QA â†’ deploy?
- [ ] Existe prÃ¡tica de shift-right / testing in production como atividade de QA?
- [ ] QA valida releases canary? (comparaÃ§Ã£o de mÃ©tricas entre o grupo canary e o restante)
- [ ] QA valida o comportamento sob feature flags? (feature ligada/desligada, rollout progressivo, kill switch)
- [ ] QA participa da validaÃ§Ã£o de testes A/B? (integridade das variaÃ§Ãµes, mÃ©tricas de sucesso)
- [ ] O monitoramento pÃ³s-release Ã© tratado formalmente como etapa de QA? (nÃ£o apenas responsabilidade de SRE/dev)

### 5.15 Time e CapacitaÃ§Ã£o de QA

- [ ] Qual a quantidade de QAs alocados na squad?
- [ ] Qual o ratio dev:QA atual? (Ã© adequado Ã  demanda?)
- [ ] Qual a senioridade dos QAs? (jÃºnior, pleno, sÃªnior, especialistas)
- [ ] Existe skills matrix do time de QA? (automaÃ§Ã£o, performance, seguranÃ§a, mobile, API, dados)
- [ ] Os QAs possuem certificaÃ§Ãµes relevantes? (CTFL/ISTQB, certificaÃ§Ãµes de ferramentas/cloud)
- [ ] Existe plano de treinamento e capacitaÃ§Ã£o contÃ­nua para o time de QA?
- [ ] Existe risco de conhecimento tribal? (dependÃªncia de pessoas-chave, bus factor)
- [ ] O conhecimento de QA estÃ¡ documentado e compartilhado? (evita silos)
- [ ] Existe plano de sucessÃ£o / backup para papÃ©is crÃ­ticos de QA?

### 5.16 Test Management e Rastreabilidade

- [ ] Existe ferramenta de gestÃ£o de casos de teste? (TestRail, Zephyr, Xray, qTest)
- [ ] Os casos de teste sÃ£o versionados e mantidos atualizados?
- [ ] Existe matriz de rastreabilidade requisito â†’ caso de teste â†’ defeito â†’ evidÃªncia?
- [ ] Como Ã© medida a cobertura de requisitos por casos de teste?
- [ ] Ã‰ possÃ­vel rastrear quais requisitos nÃ£o possuem casos de teste associados?
- [ ] As execuÃ§Ãµes de teste ficam registradas com evidÃªncias vinculadas aos casos?
- [ ] A ferramenta de gestÃ£o de testes estÃ¡ integrada Ã  gestÃ£o de defeitos e ao backlog? (Jira, etc.)
- [ ] Existe organizaÃ§Ã£o dos casos de teste por suÃ­tes/features/regressÃ£o?

### 5.17 Cobertura Funcional do Extrato (Regras de NegÃ³cio)

- [ ] Filtros por perÃ­odo sÃ£o testados? (dia, semana, mÃªs, perÃ­odo customizado, limites de intervalo)
- [ ] A categorizaÃ§Ã£o de lanÃ§amentos Ã© testada? (crÃ©dito/dÃ©bito, categorias, tags)
- [ ] A exportaÃ§Ã£o do extrato Ã© testada em todos os formatos? (PDF, OFX, CSV)
- [ ] A geraÃ§Ã£o e visualizaÃ§Ã£o de comprovantes Ã© testada?
- [ ] O cÃ¡lculo e a exibiÃ§Ã£o do saldo sÃ£o testados? (saldo disponÃ­vel, bloqueado, atual)
- [ ] LanÃ§amentos futuros/agendados sÃ£o testados? (exibiÃ§Ã£o, efetivaÃ§Ã£o, cancelamento)
- [ ] TransaÃ§Ãµes PIX sÃ£o testadas no extrato? (enviado, recebido, devolvido, agendado)
- [ ] Tarifas sÃ£o testadas? (cobranÃ§a, exibiÃ§Ã£o, isenÃ§Ãµes)
- [ ] Estornos e cancelamentos sÃ£o testados? (reflexo no saldo e no extrato)
- [ ] A ordenaÃ§Ã£o e o agrupamento de transaÃ§Ãµes sÃ£o testados? (por data, valor, tipo; agrupamento por dia/categoria)
- [ ] A consistÃªncia entre saldo e a soma dos lanÃ§amentos Ã© validada?

### 5.18 EstratÃ©gia de Teste do Portal Web

- [ ] Existe estratÃ©gia de teste cross-browser? (Chrome, Edge, Safari, Firefox)
- [ ] Quais versÃµes de navegadores sÃ£o suportadas e testadas?
- [ ] SÃ£o realizados testes de responsividade web? (desktop, tablet, diferentes resoluÃ§Ãµes)
- [ ] Existem testes cross-channel? (jornada iniciada no mobile e continuada no web, e vice-versa)
- [ ] A consistÃªncia de dados entre canais Ã© validada? (mesmo extrato/saldo no mobile e no web)
- [ ] A consistÃªncia de experiÃªncia entre canais Ã© validada? (funcionalidades equivalentes, paridade de features)
- [ ] Existe automaÃ§Ã£o de testes web? (Cypress, Playwright, Selenium)
- [ ] Como Ã© garantida a paridade funcional entre o portal web e o APP mobile?

---

## 6. Itens a Levantar â€” Engenheiro de Desenvolvimento (Engenheiro de Desenvolvimento)

### 6.1 Arquitetura de Software

- [ ] Qual a arquitetura do APP mobile? (nativo, hÃ­brido, cross-platform)
- [ ] Plataformas suportadas (iOS, Android, versÃµes mÃ­nimas)
- [ ] Arquitetura do backend (monolito, microsserviÃ§os, serverless, event-driven)
- [ ] Existe BFF (Backend for Frontend)?
- [ ] Como Ã© a comunicaÃ§Ã£o mobile â†” backend? (REST, GraphQL, gRPC, WebSocket)
- [ ] Existe arquitetura documentada (C4 Model, diagramas de contexto, componentes)?
- [ ] Quais integraÃ§Ãµes existem? (core banking, mainframe, APIs de terceiros)
- [ ] Existe API Gateway? Qual?
- [ ] Como Ã© o gerenciamento de estado no mobile?

### 6.2 Stack TecnolÃ³gica

- [ ] Linguagens utilizadas (mobile: Swift, Kotlin, React Native, Flutter; backend: Java, Node.js, Go, etc.)
- [ ] Frameworks e bibliotecas principais
- [ ] Banco de dados utilizado (relacional, NoSQL, cache)
- [ ] Mensageria (Kafka, RabbitMQ, SQS, etc.)
- [ ] Ferramentas de observabilidade (Datadog, Dynatrace, Splunk, Grafana, etc.)
- [ ] Stack do portal web (React, Angular, Vue, etc.)

### 6.3 RepositÃ³rios e Versionamento

- [ ] Onde fica o cÃ³digo? (GitHub, GitLab, Bitbucket, Azure DevOps)
- [ ] EstratÃ©gia de branching (GitFlow, trunk-based, feature flags)
- [ ] Existe mono-repo ou multi-repo?
- [ ] Como Ã© feito o code review? (pull requests, pair programming)
- [ ] Existem padrÃµes de commit? (conventional commits)
- [ ] Existe linting e formataÃ§Ã£o automatizada?

### 6.4 CI/CD e DevOps

- [ ] Qual ferramenta de CI/CD? (Jenkins, GitHub Actions, GitLab CI, Azure Pipelines)
- [ ] Como Ã© o pipeline? (build â†’ testes â†’ anÃ¡lise estÃ¡tica â†’ deploy)
- [ ] FrequÃªncia de deploys (diÃ¡rio, semanal, quinzenal, por sprint)
- [ ] Existe deploy automatizado ou hÃ¡ gates manuais?
- [ ] Como funciona o rollback?
- [ ] Existe feature flag / toggle? Qual ferramenta?
- [ ] Como Ã© publicado o APP nas stores? (manual, Fastlane, App Center)
- [ ] Existe blue/green ou canary deployment?

### 6.5 SeguranÃ§a no Desenvolvimento

- [ ] Existe SAST integrado ao pipeline? (SonarQube, Checkmarx, Fortify)
- [ ] Existe DAST? (OWASP ZAP, Burp)
- [ ] Existe SCA (Software Composition Analysis) para dependÃªncias?
- [ ] Como Ã© feita a gestÃ£o de secrets? (Vault, AWS Secrets Manager, variÃ¡veis de CI)
- [ ] Existe code signing para os apps mobile?
- [ ] Existe processo de security review?

### 6.6 Arquitetura de Infraestrutura

- [ ] Cloud provider (AWS, Azure, GCP, on-premise, hÃ­brido)
- [ ] Containers? (Docker, Kubernetes, ECS)
- [ ] IaC? (Terraform, CloudFormation, Pulumi)
- [ ] CDN para assets?
- [ ] EstratÃ©gia de escalabilidade

### 6.7 PadrÃµes e Boas PrÃ¡ticas de CÃ³digo

- [ ] Existe guia de estilo / coding standards documentado?
- [ ] PadrÃµes de arquitetura no mobile (MVVM, Clean Architecture, MVI)
- [ ] PadrÃµes de arquitetura no backend (DDD, hexagonal, clean)
- [ ] Existe ADR (Architecture Decision Records)?
- [ ] Como Ã© tratado dÃ©bito tÃ©cnico? Existe backlog priorizado?
- [ ] Existe documentaÃ§Ã£o de APIs? (Swagger/OpenAPI, AsyncAPI)

### 6.8 DocumentaÃ§Ã£o TÃ©cnica

- [ ] Existe documentaÃ§Ã£o de onboarding para novos devs?
- [ ] Diagramas de sequÃªncia dos principais fluxos (extrato, filtros, comprovantes)
- [ ] Existe runbook para incidentes?
- [ ] DocumentaÃ§Ã£o de integraÃ§Ãµes estÃ¡ atualizada?
- [ ] Onde fica a documentaÃ§Ã£o tÃ©cnica? (repo, wiki, Confluence)

### 6.9 Observabilidade e Monitoramento

- [ ] Existe APM (Application Performance Monitoring)?
- [ ] Logs estruturados? CentralizaÃ§Ã£o de logs?
- [ ] Distributed tracing?
- [ ] Alertas configurados? (latÃªncia, erro rate, disponibilidade)
- [ ] SLIs/SLOs definidos para o extrato?
- [ ] Existe crash reporting para mobile? (Crashlytics, Sentry)

---

## 7. Itens Compartilhados (Engenheiro de Qualidade + Engenheiro de Desenvolvimento)

### 7.1 Processo de Desenvolvimento (VisÃ£o Geral)

- [ ] Qual metodologia Ã¡gil Ã© utilizada? (Scrum, Kanban, SAFe, hÃ­brido)
- [ ] DuraÃ§Ã£o da sprint / cadÃªncia de entregas
- [ ] Quais cerimÃ´nias sÃ£o realizadas? (planning, daily, review, retro, refinement)
- [ ] Como Ã© o fluxo de uma demanda? (ideaÃ§Ã£o â†’ refinamento â†’ dev â†’ QA â†’ deploy â†’ monitoramento)
- [ ] Existe Kanban board? Qual ferramenta? (Jira, Azure Boards, Linear)
- [ ] Quais mÃ©tricas de fluxo sÃ£o acompanhadas? (lead time, cycle time, throughput, WIP)

### 7.2 GestÃ£o de Requisitos e DocumentaÃ§Ã£o Funcional

- [ ] Como chegam as demandas para a squad?
- [ ] Quem escreve as histÃ³rias de usuÃ¡rio?
- [ ] Existe documentaÃ§Ã£o funcional das features de extrato?
- [ ] Existe mapeamento de jornadas do usuÃ¡rio?
- [ ] Como Ã© feito o refinamento tÃ©cnico?

### 7.3 ComunicaÃ§Ã£o e ColaboraÃ§Ã£o

- [ ] Canais de comunicaÃ§Ã£o (Slack, Teams, etc.)
- [ ] Como Ã© a interaÃ§Ã£o com outras squads / dependÃªncias?
- [ ] Existe documentaÃ§Ã£o de interfaces entre squads?
- [ ] Como sÃ£o tratadas dependÃªncias externas?

### 7.4 GestÃ£o de Incidentes

- [ ] Existe processo de incident management?
- [ ] Como Ã© o war room / resposta a incidentes?
- [ ] Existe post-mortem / blameless retrospective?
- [ ] Qual o MTTR (Mean Time to Recovery) atual?

---

## 8. Artefatos a Coletar

| Artefato | ResponsÃ¡vel |
|----------|-------------|
| Diagrama de arquitetura atual | Engenheiro de Desenvolvimento |
| Pipeline de CI/CD (screenshot ou YAML) | Engenheiro de Desenvolvimento |
| Lista de repositÃ³rios e owners | Engenheiro de Desenvolvimento |
| EstratÃ©gia de testes documentada | Engenheiro de Qualidade |
| RelatÃ³rios de cobertura de testes | Engenheiro de Qualidade |
| Dashboard de mÃ©tricas de qualidade | Engenheiro de Qualidade |
| Board do Jira / ferramenta de gestÃ£o | Engenheiro de Qualidade + Engenheiro de Desenvolvimento |
| DocumentaÃ§Ã£o funcional existente | Engenheiro de Qualidade + Engenheiro de Desenvolvimento |
| RelatÃ³rios de incidentes recentes | Engenheiro de Qualidade + Engenheiro de Desenvolvimento |
| DocumentaÃ§Ã£o de APIs (Swagger/OpenAPI) | Engenheiro de Desenvolvimento |
| RelatÃ³rios de seguranÃ§a (SAST/DAST) | Engenheiro de Desenvolvimento |
| Casos de teste / cenÃ¡rios automatizados | Engenheiro de Qualidade |
| MÃ©tricas de fluxo (lead time, cycle time) | Engenheiro de Qualidade + Engenheiro de Desenvolvimento |
| Runbooks e playbooks de incidentes | Engenheiro de Desenvolvimento |

---

## 9. Cronograma Sugerido

| Fase | DuraÃ§Ã£o | Atividade |
|------|---------|-----------|
| Semana 1 | 5 dias | Kickoff, alinhamento, agendamento de entrevistas |
| Semana 2-3 | 10 dias | Entrevistas e coleta de artefatos (AS IS) |
| Semana 4 | 5 dias | ConsolidaÃ§Ã£o do AS IS, identificaÃ§Ã£o de gaps |
| Semana 5 | 5 dias | Desenho do TO BE com recomendaÃ§Ãµes |
| Semana 6 | 5 dias | ValidaÃ§Ã£o com stakeholders, plano de aÃ§Ã£o |

---

## 10. EntregÃ¡veis Finais

1. **Documento AS IS** â€” Estado atual detalhado de processos, arquitetura, qualidade e ferramentas
2. **Gap Analysis** â€” Lacunas identificadas entre o estado atual e as melhores prÃ¡ticas de mercado
3. **Documento TO BE** â€” Estado desejado com recomendaÃ§Ãµes priorizadas
4. **Roadmap de EvoluÃ§Ã£o** â€” Plano de aÃ§Ã£o com quick wins e iniciativas de mÃ©dio/longo prazo
5. **Matriz de Riscos** â€” Riscos identificados e mitigaÃ§Ãµes propostas

---

## 11. CritÃ©rios de AvaliaÃ§Ã£o (Maturidade)

Para cada dimensÃ£o, classificar em nÃ­veis:

| NÃ­vel | DescriÃ§Ã£o |
|-------|-----------|
| 1 - Inicial | Processos ad-hoc, sem padronizaÃ§Ã£o |
| 2 - RepetÃ­vel | Processos bÃ¡sicos definidos, execuÃ§Ã£o inconsistente |
| 3 - Definido | Processos documentados e seguidos |
| 4 - Gerenciado | Processos medidos e controlados |
| 5 - Otimizado | Melhoria contÃ­nua baseada em dados |

### DimensÃµes a avaliar:
- GestÃ£o de Requisitos
- Arquitetura e Design
- Desenvolvimento e Code Quality
- Testes e Qualidade
- CI/CD e DevOps
- SeguranÃ§a (DevSecOps)
- Observabilidade e Monitoramento
- DocumentaÃ§Ã£o
- GestÃ£o de Incidentes
- Processos Ãgeis e Fluxo

---

*Documento gerado para assessment da Squad Extrato â€” Ciclo de Desenvolvimento de Software*
