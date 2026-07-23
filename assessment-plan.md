# Assessment do Ciclo de Desenvolvimento de Software
## Squad Extrato - APP Bancário (Mobile + Portal Web)

---

## 1. Objetivo

Mapear o estado atual (AS IS) e desenhar o estado desejado (TO BE) do ciclo de desenvolvimento de software da Squad Extrato, cobrindo documentação, processos, arquitetura, tecnologias, qualidade e entrega.

---

## 2. Escopo

- Funcionalidades de extrato no APP mobile do banco
- Portal web do banco (em desenho/evolução)
- Todo o ciclo de vida do software: ideação → desenvolvimento → testes → deploy → monitoramento

---

## 3. Divisão de Responsabilidades

| Área | Responsável |
|------|-------------|
| Qualidade, Testes, Processos de QA, Métricas de Defeitos | Fulano 1 (Engenheiro de Qualidade) |
| Desenvolvimento, Arquitetura, DevOps, Código, Frameworks | Fulano 2 (Engenheiro de Desenvolvimento) |

---

## 4. Stakeholders a Entrevistar

| Pessoa/Papel | Tópicos | Quem entrevista |
|--------------|---------|-----------------|
| Tech Lead / Líder Técnico da Squad | Arquitetura, decisões técnicas, débitos técnicos, roadmap | Fulano 2 |
| Product Owner (PO) | Backlog, priorização, requisitos, fluxo de demandas | Fulano 1 + Fulano 2 |
| Scrum Master / Agile Coach | Cerimônias, métricas de fluxo, impedimentos recorrentes | Fulano 1 + Fulano 2 |
| Desenvolvedores Mobile (iOS/Android) | Stack, padrões, code review, CI/CD, testes unitários | Fulano 2 |
| Desenvolvedores Backend/APIs | Stack, contratos de API, integrações, observabilidade | Fulano 2 |
| Desenvolvedores Frontend Web | Stack web, design system, acessibilidade | Fulano 2 |
| QA / Analistas de Teste da Squad | Estratégia de testes, automação, ambientes, cobertura | Fulano 1 |
| DevOps / SRE | Pipelines, infra, deploys, rollback, monitoramento | Fulano 2 |
| Arquiteto de Soluções (se existir) | Visão macro, integrações entre sistemas, conformidade | Fulano 2 |
| UX/UI Designer | Fluxo de entrega de design, handoff, design system | Fulano 1 + Fulano 2 |
| Segurança da Informação (AppSec) | SAST/DAST, políticas de segurança, compliance | Fulano 1 + Fulano 2 |
| Gestor da área / Coordenação | Expectativas, metas, dores estratégicas | Fulano 1 + Fulano 2 |

---

## 5. Itens a Levantar — Fulano 1 (Engenheiro de Qualidade)

### 5.1 Processos de Qualidade

- [ ] Existe estratégia de teste documentada?
- [ ] Quais tipos de teste são executados? (unitário, integração, E2E, regressão, performance, segurança, acessibilidade)
- [ ] Qual a cobertura de testes automatizados atual?
- [ ] Existe pirâmide de testes definida?
- [ ] Como é feita a gestão de defeitos? (ferramenta, fluxo, SLA)
- [ ] Existe processo de teste exploratório?
- [ ] Como são tratados os bugs em produção? (hotfix, rollback, comunicação)
- [ ] Existe classificação de defeitos por severidade e prioridade? (matriz severidade × prioridade)
- [ ] Como é definida a severidade de um defeito? (impacto no negócio, no cliente, financeiro)
- [ ] É realizada análise de causa raiz (RCA — Root Cause Analysis) para defeitos críticos?
- [ ] Existe análise de reincidência de defeitos? (defeitos recorrentes, mesmo módulo/causa)
- [ ] Como os aprendizados dos RCAs realimentam a prevenção? (ações corretivas, testes adicionais)

### 5.2 Automação de Testes

- [ ] Quais frameworks de automação são utilizados? (mobile, API, web)
- [ ] Existe automação de testes de regressão?
- [ ] Qual a frequência de execução dos testes automatizados?
- [ ] Os testes estão integrados ao pipeline de CI/CD?
- [ ] Existe teste de contrato (contract testing) para APIs?
- [ ] Ferramentas utilizadas (Appium, Detox, Cypress, Selenium, Postman, K6, JMeter, etc.)
- [ ] Existe controle de testes instáveis (flaky tests)? Como são identificados e tratados?
- [ ] Existe processo de quarentena para testes instáveis?
- [ ] Qual o tempo de execução da suíte automatizada? (é aceitável para o ciclo de entrega?)
- [ ] Qual a confiabilidade da suíte? (taxa de falsos positivos/negativos)
- [ ] Qual o custo/esforço de manutenção da automação? (frequência de quebras, refatorações)
- [ ] Existe estratégia para manter a saúde da suíte ao longo do tempo? (revisão, deprecação de testes obsoletos)

### 5.3 Ambientes de Teste

- [ ] Quantos ambientes existem? (dev, QA, staging, homologação, produção)
- [ ] Como é feita a gestão de dados de teste?
- [ ] Existe massa de dados anonimizada/sintética?
- [ ] Os ambientes são estáveis e representativos de produção?
- [ ] Existe ambiente de performance isolado?

### 5.4 Métricas de Qualidade

- [ ] Quais métricas são acompanhadas? (taxa de defeitos, escape rate, MTTR, cobertura, etc.)
- [ ] Existe dashboard de qualidade?
- [ ] Qual o histórico de incidentes em produção nos últimos 6 meses?
- [ ] Qual o lead time de correção de bugs?
- [ ] Existem quality gates objetivos definidos? (critérios de bloqueio de release)
- [ ] Quais critérios bloqueiam um release? (cobertura mínima, zero defeitos críticos/bloqueantes, testes verdes)
- [ ] Os quality gates estão automatizados no pipeline ou são verificados manualmente?
- [ ] Existem valores-alvo (targets) definidos para as métricas no TO BE? (ex.: cobertura ≥ 80%, escape rate < X%, MTTR < Y)
- [ ] Como os targets são acompanhados e revisados ao longo do tempo?

### 5.5 Processos e Documentação

- [ ] Existe Definition of Ready (DoR) e Definition of Done (DoD)?
- [ ] Os critérios de aceite são claros nas histórias?
- [ ] Existe processo de review de qualidade antes do deploy?
- [ ] Como funciona o processo de homologação com o PO/negócio?
- [ ] Existe documentação de cenários de teste (casos de teste, BDD, etc.)?
- [ ] Onde fica a documentação? (Confluence, Notion, Wiki, repositório)
- [ ] Existe processo formal de UAT / homologação com o negócio?
- [ ] Quem homologa as entregas? (PO, negócio, key users)
- [ ] Os critérios de aceite formais estão definidos e acordados antes da homologação?
- [ ] Existe registro formal de sign-off da homologação? (evidência de aprovação)
- [ ] Como é feita a gestão do ambiente de homologação com o negócio? (acesso, massa, disponibilidade)
- [ ] Existe SLA/prazo definido para o ciclo de homologação?

### 5.6 Compliance e Regulatório

- [ ] Existem testes específicos para requisitos regulatórios (BACEN, LGPD)?
- [ ] Como é garantida a conformidade com normas de segurança?
- [ ] Existe auditoria de testes / evidências de execução?
- [ ] Existem testes específicos para requisitos de Open Finance / Open Banking?
- [ ] Como é validada a conformidade no compartilhamento de dados de extrato? (consentimento, escopo, prazo)
- [ ] Existem testes de consentimento e revogação de compartilhamento de dados?
- [ ] Os dados compartilhados via Open Finance são consistentes com o extrato exibido nos canais próprios?
- [ ] Existem testes de conformidade com os padrões e APIs do Open Finance Brasil?

### 5.7 Testes Não Funcionais — Performance

- [ ] Existe estratégia de testes de performance documentada?
- [ ] Quais tipos de teste de performance são executados? (carga, estresse, pico, endurance/soak, escalabilidade)
- [ ] Quais ferramentas são utilizadas? (JMeter, Gatling, K6, Locust, Artillery, NeoLoad)
- [ ] Existe baseline de performance definida? (tempo de resposta aceitável para o extrato, throughput mínimo)
- [ ] Os testes de performance são executados em ambiente dedicado ou compartilhado?
- [ ] Existe monitoramento de performance no mobile? (tempo de renderização, consumo de memória, CPU, bateria)
- [ ] Como são definidos os SLAs de performance para o extrato? (ex.: carregamento em < 2s no P95)
- [ ] Existe teste de performance integrado ao pipeline de CI/CD?
- [ ] São realizados testes de capacidade antes de grandes releases ou campanhas?
- [ ] Existe análise de degradação de performance entre versões?

### 5.8 Testes Não Funcionais — Data Test (Qualidade de Dados)

- [ ] Existe estratégia de validação/qualidade de dados?
- [ ] Como é garantida a integridade dos dados do extrato? (consistência entre core banking e APP)
- [ ] Existem testes de validação de dados ponta a ponta? (origem → API → apresentação no APP)
- [ ] Existe monitoramento de data quality em produção? (dados ausentes, duplicados, inconsistentes)
- [ ] Como é validada a precisão dos valores monetários no extrato? (casas decimais, arredondamento, moeda)
- [ ] Existem testes de migração de dados?
- [ ] Existe validação de dados em cenários de alta volumetria? (contas com milhares de transações)
- [ ] Como é tratada a paginação e lazy loading no extrato com grandes volumes?
- [ ] Existe teste de reconciliação entre dados exibidos no APP vs. portal web vs. core banking?
- [ ] Como é garantida a conformidade LGPD nos dados de teste? (anonimização, mascaramento)

### 5.9 Testes Não Funcionais — Segurança

- [ ] Existem testes de segurança específicos para o APP mobile? (OWASP Mobile Top 10)
- [ ] É realizado pentest periódico na funcionalidade de extrato?
- [ ] Existem testes de autenticação e autorização? (token expirado, session hijacking, privilege escalation)
- [ ] São testados cenários de vazamento de dados sensíveis? (logs, cache, screenshots do extrato)
- [ ] Existe validação de criptografia em trânsito e em repouso?
- [ ] Testes de certificate pinning são realizados?
- [ ] Como é testada a proteção contra scraping/automação maliciosa no extrato?

### 5.10 Testes Não Funcionais — Acessibilidade

- [ ] Existe estratégia de testes de acessibilidade?
- [ ] Quais guidelines são seguidos? (WCAG 2.1, diretrizes de acessibilidade iOS/Android)
- [ ] São realizados testes com leitores de tela? (VoiceOver, TalkBack)
- [ ] Existe validação de contraste, tamanhos de fonte e áreas de toque?
- [ ] A funcionalidade de extrato é navegável via teclado / controles alternativos?
- [ ] Existe automação de testes de acessibilidade? (axe, Accessibility Scanner)

### 5.11 Testes Não Funcionais — Usabilidade e Compatibilidade

- [ ] Existe matrix de dispositivos/OS suportados para testes?
- [ ] São realizados testes em dispositivos reais ou apenas emuladores?
- [ ] Existe device farm? (BrowserStack, AWS Device Farm, Samsung Remote Test Lab)
- [ ] Como é testada a compatibilidade com diferentes resoluções e tamanhos de tela?
- [ ] São realizados testes de comportamento offline / conectividade intermitente?
- [ ] Existe teste de instalação, atualização e migração de versão do APP?
- [ ] São testados cenários de interrupção? (chamada telefônica, notificação, multitasking)

### 5.12 Testes Não Funcionais — Confiabilidade e Resiliência

- [ ] Existem testes de resiliência / chaos engineering?
- [ ] São testados cenários de falha de dependências? (API indisponível, timeout, core banking fora)
- [ ] Como é validado o comportamento do APP em cenários de erro? (mensagens amigáveis, retry, fallback)
- [ ] Existe teste de recuperação após falhas? (crash recovery, persistência de estado)
- [ ] São realizados testes de concorrência? (múltiplas sessões, race conditions)
- [ ] Existe SLA de disponibilidade definido e testado para o extrato?

### 5.13 Testes Não Funcionais — Observabilidade e Monitoramento (visão QA)

- [ ] QA valida que os logs e traces estão sendo gerados corretamente?
- [ ] Existe teste de alertas? (o alerta dispara corretamente quando o SLO é violado?)
- [ ] QA participa da definição de SLIs/SLOs?
- [ ] Existem testes de synthetic monitoring para o extrato?
- [ ] Como QA monitora a saúde da feature em produção pós-deploy?
- [ ] QA acompanha métricas e alertas nas primeiras horas após o release? (monitoramento pós-release ativo)
- [ ] Existem critérios objetivos para abortar/reverter um release com base em observabilidade?

### 5.14 Processo de Desenvolvimento (visão QA)

- [ ] Em que momento QA entra no ciclo? (shift-left?)
- [ ] QA participa do refinamento e planning?
- [ ] Existe pair testing ou mob testing?
- [ ] Como é o handoff dev → QA → deploy?
- [ ] Existe prática de shift-right / testing in production como atividade de QA?
- [ ] QA valida releases canary? (comparação de métricas entre o grupo canary e o restante)
- [ ] QA valida o comportamento sob feature flags? (feature ligada/desligada, rollout progressivo, kill switch)
- [ ] QA participa da validação de testes A/B? (integridade das variações, métricas de sucesso)
- [ ] O monitoramento pós-release é tratado formalmente como etapa de QA? (não apenas responsabilidade de SRE/dev)

### 5.15 Time e Capacitação de QA

- [ ] Qual a quantidade de QAs alocados na squad?
- [ ] Qual o ratio dev:QA atual? (é adequado à demanda?)
- [ ] Qual a senioridade dos QAs? (júnior, pleno, sênior, especialistas)
- [ ] Existe skills matrix do time de QA? (automação, performance, segurança, mobile, API, dados)
- [ ] Os QAs possuem certificações relevantes? (CTFL/ISTQB, certificações de ferramentas/cloud)
- [ ] Existe plano de treinamento e capacitação contínua para o time de QA?
- [ ] Existe risco de conhecimento tribal? (dependência de pessoas-chave, bus factor)
- [ ] O conhecimento de QA está documentado e compartilhado? (evita silos)
- [ ] Existe plano de sucessão / backup para papéis críticos de QA?

### 5.16 Test Management e Rastreabilidade

- [ ] Existe ferramenta de gestão de casos de teste? (TestRail, Zephyr, Xray, qTest)
- [ ] Os casos de teste são versionados e mantidos atualizados?
- [ ] Existe matriz de rastreabilidade requisito → caso de teste → defeito → evidência?
- [ ] Como é medida a cobertura de requisitos por casos de teste?
- [ ] É possível rastrear quais requisitos não possuem casos de teste associados?
- [ ] As execuções de teste ficam registradas com evidências vinculadas aos casos?
- [ ] A ferramenta de gestão de testes está integrada à gestão de defeitos e ao backlog? (Jira, etc.)
- [ ] Existe organização dos casos de teste por suítes/features/regressão?

### 5.17 Cobertura Funcional do Extrato (Regras de Negócio)

- [ ] Filtros por período são testados? (dia, semana, mês, período customizado, limites de intervalo)
- [ ] A categorização de lançamentos é testada? (crédito/débito, categorias, tags)
- [ ] A exportação do extrato é testada em todos os formatos? (PDF, OFX, CSV)
- [ ] A geração e visualização de comprovantes é testada?
- [ ] O cálculo e a exibição do saldo são testados? (saldo disponível, bloqueado, atual)
- [ ] Lançamentos futuros/agendados são testados? (exibição, efetivação, cancelamento)
- [ ] Transações PIX são testadas no extrato? (enviado, recebido, devolvido, agendado)
- [ ] Tarifas são testadas? (cobrança, exibição, isenções)
- [ ] Estornos e cancelamentos são testados? (reflexo no saldo e no extrato)
- [ ] A ordenação e o agrupamento de transações são testados? (por data, valor, tipo; agrupamento por dia/categoria)
- [ ] A consistência entre saldo e a soma dos lançamentos é validada?

### 5.18 Estratégia de Teste do Portal Web

- [ ] Existe estratégia de teste cross-browser? (Chrome, Edge, Safari, Firefox)
- [ ] Quais versões de navegadores são suportadas e testadas?
- [ ] São realizados testes de responsividade web? (desktop, tablet, diferentes resoluções)
- [ ] Existem testes cross-channel? (jornada iniciada no mobile e continuada no web, e vice-versa)
- [ ] A consistência de dados entre canais é validada? (mesmo extrato/saldo no mobile e no web)
- [ ] A consistência de experiência entre canais é validada? (funcionalidades equivalentes, paridade de features)
- [ ] Existe automação de testes web? (Cypress, Playwright, Selenium)
- [ ] Como é garantida a paridade funcional entre o portal web e o APP mobile?

---

## 6. Itens a Levantar — Fulano 2 (Engenheiro de Desenvolvimento)

### 6.1 Arquitetura de Software

- [ ] Qual a arquitetura do APP mobile? (nativo, híbrido, cross-platform)
- [ ] Plataformas suportadas (iOS, Android, versões mínimas)
- [ ] Arquitetura do backend (monolito, microsserviços, serverless, event-driven)
- [ ] Existe BFF (Backend for Frontend)?
- [ ] Como é a comunicação mobile ↔ backend? (REST, GraphQL, gRPC, WebSocket)
- [ ] Existe arquitetura documentada (C4 Model, diagramas de contexto, componentes)?
- [ ] Quais integrações existem? (core banking, mainframe, APIs de terceiros)
- [ ] Existe API Gateway? Qual?
- [ ] Como é o gerenciamento de estado no mobile?

### 6.2 Stack Tecnológica

- [ ] Linguagens utilizadas (mobile: Swift, Kotlin, React Native, Flutter; backend: Java, Node.js, Go, etc.)
- [ ] Frameworks e bibliotecas principais
- [ ] Banco de dados utilizado (relacional, NoSQL, cache)
- [ ] Mensageria (Kafka, RabbitMQ, SQS, etc.)
- [ ] Ferramentas de observabilidade (Datadog, Dynatrace, Splunk, Grafana, etc.)
- [ ] Stack do portal web (React, Angular, Vue, etc.)

### 6.3 Repositórios e Versionamento

- [ ] Onde fica o código? (GitHub, GitLab, Bitbucket, Azure DevOps)
- [ ] Estratégia de branching (GitFlow, trunk-based, feature flags)
- [ ] Existe mono-repo ou multi-repo?
- [ ] Como é feito o code review? (pull requests, pair programming)
- [ ] Existem padrões de commit? (conventional commits)
- [ ] Existe linting e formatação automatizada?

### 6.4 CI/CD e DevOps

- [ ] Qual ferramenta de CI/CD? (Jenkins, GitHub Actions, GitLab CI, Azure Pipelines)
- [ ] Como é o pipeline? (build → testes → análise estática → deploy)
- [ ] Frequência de deploys (diário, semanal, quinzenal, por sprint)
- [ ] Existe deploy automatizado ou há gates manuais?
- [ ] Como funciona o rollback?
- [ ] Existe feature flag / toggle? Qual ferramenta?
- [ ] Como é publicado o APP nas stores? (manual, Fastlane, App Center)
- [ ] Existe blue/green ou canary deployment?

### 6.5 Segurança no Desenvolvimento

- [ ] Existe SAST integrado ao pipeline? (SonarQube, Checkmarx, Fortify)
- [ ] Existe DAST? (OWASP ZAP, Burp)
- [ ] Existe SCA (Software Composition Analysis) para dependências?
- [ ] Como é feita a gestão de secrets? (Vault, AWS Secrets Manager, variáveis de CI)
- [ ] Existe code signing para os apps mobile?
- [ ] Existe processo de security review?

### 6.6 Arquitetura de Infraestrutura

- [ ] Cloud provider (AWS, Azure, GCP, on-premise, híbrido)
- [ ] Containers? (Docker, Kubernetes, ECS)
- [ ] IaC? (Terraform, CloudFormation, Pulumi)
- [ ] CDN para assets?
- [ ] Estratégia de escalabilidade

### 6.7 Padrões e Boas Práticas de Código

- [ ] Existe guia de estilo / coding standards documentado?
- [ ] Padrões de arquitetura no mobile (MVVM, Clean Architecture, MVI)
- [ ] Padrões de arquitetura no backend (DDD, hexagonal, clean)
- [ ] Existe ADR (Architecture Decision Records)?
- [ ] Como é tratado débito técnico? Existe backlog priorizado?
- [ ] Existe documentação de APIs? (Swagger/OpenAPI, AsyncAPI)

### 6.8 Documentação Técnica

- [ ] Existe documentação de onboarding para novos devs?
- [ ] Diagramas de sequência dos principais fluxos (extrato, filtros, comprovantes)
- [ ] Existe runbook para incidentes?
- [ ] Documentação de integrações está atualizada?
- [ ] Onde fica a documentação técnica? (repo, wiki, Confluence)

### 6.9 Observabilidade e Monitoramento

- [ ] Existe APM (Application Performance Monitoring)?
- [ ] Logs estruturados? Centralização de logs?
- [ ] Distributed tracing?
- [ ] Alertas configurados? (latência, erro rate, disponibilidade)
- [ ] SLIs/SLOs definidos para o extrato?
- [ ] Existe crash reporting para mobile? (Crashlytics, Sentry)

---

## 7. Itens Compartilhados (Fulano 1 + Fulano 2)

### 7.1 Processo de Desenvolvimento (Visão Geral)

- [ ] Qual metodologia ágil é utilizada? (Scrum, Kanban, SAFe, híbrido)
- [ ] Duração da sprint / cadência de entregas
- [ ] Quais cerimônias são realizadas? (planning, daily, review, retro, refinement)
- [ ] Como é o fluxo de uma demanda? (ideação → refinamento → dev → QA → deploy → monitoramento)
- [ ] Existe Kanban board? Qual ferramenta? (Jira, Azure Boards, Linear)
- [ ] Quais métricas de fluxo são acompanhadas? (lead time, cycle time, throughput, WIP)

### 7.2 Gestão de Requisitos e Documentação Funcional

- [ ] Como chegam as demandas para a squad?
- [ ] Quem escreve as histórias de usuário?
- [ ] Existe documentação funcional das features de extrato?
- [ ] Existe mapeamento de jornadas do usuário?
- [ ] Como é feito o refinamento técnico?

### 7.3 Comunicação e Colaboração

- [ ] Canais de comunicação (Slack, Teams, etc.)
- [ ] Como é a interação com outras squads / dependências?
- [ ] Existe documentação de interfaces entre squads?
- [ ] Como são tratadas dependências externas?

### 7.4 Gestão de Incidentes

- [ ] Existe processo de incident management?
- [ ] Como é o war room / resposta a incidentes?
- [ ] Existe post-mortem / blameless retrospective?
- [ ] Qual o MTTR (Mean Time to Recovery) atual?

---

## 8. Artefatos a Coletar

| Artefato | Responsável |
|----------|-------------|
| Diagrama de arquitetura atual | Fulano 2 |
| Pipeline de CI/CD (screenshot ou YAML) | Fulano 2 |
| Lista de repositórios e owners | Fulano 2 |
| Estratégia de testes documentada | Fulano 1 |
| Relatórios de cobertura de testes | Fulano 1 |
| Dashboard de métricas de qualidade | Fulano 1 |
| Board do Jira / ferramenta de gestão | Fulano 1 + Fulano 2 |
| Documentação funcional existente | Fulano 1 + Fulano 2 |
| Relatórios de incidentes recentes | Fulano 1 + Fulano 2 |
| Documentação de APIs (Swagger/OpenAPI) | Fulano 2 |
| Relatórios de segurança (SAST/DAST) | Fulano 2 |
| Casos de teste / cenários automatizados | Fulano 1 |
| Métricas de fluxo (lead time, cycle time) | Fulano 1 + Fulano 2 |
| Runbooks e playbooks de incidentes | Fulano 2 |

---

## 9. Cronograma Sugerido

| Fase | Duração | Atividade |
|------|---------|-----------|
| Semana 1 | 5 dias | Kickoff, alinhamento, agendamento de entrevistas |
| Semana 2-3 | 10 dias | Entrevistas e coleta de artefatos (AS IS) |
| Semana 4 | 5 dias | Consolidação do AS IS, identificação de gaps |
| Semana 5 | 5 dias | Desenho do TO BE com recomendações |
| Semana 6 | 5 dias | Validação com stakeholders, plano de ação |

---

## 10. Entregáveis Finais

1. **Documento AS IS** — Estado atual detalhado de processos, arquitetura, qualidade e ferramentas
2. **Gap Analysis** — Lacunas identificadas entre o estado atual e as melhores práticas de mercado
3. **Documento TO BE** — Estado desejado com recomendações priorizadas
4. **Roadmap de Evolução** — Plano de ação com quick wins e iniciativas de médio/longo prazo
5. **Matriz de Riscos** — Riscos identificados e mitigações propostas

---

## 11. Critérios de Avaliação (Maturidade)

Para cada dimensão, classificar em níveis:

| Nível | Descrição |
|-------|-----------|
| 1 - Inicial | Processos ad-hoc, sem padronização |
| 2 - Repetível | Processos básicos definidos, execução inconsistente |
| 3 - Definido | Processos documentados e seguidos |
| 4 - Gerenciado | Processos medidos e controlados |
| 5 - Otimizado | Melhoria contínua baseada em dados |

### Dimensões a avaliar:
- Gestão de Requisitos
- Arquitetura e Design
- Desenvolvimento e Code Quality
- Testes e Qualidade
- CI/CD e DevOps
- Segurança (DevSecOps)
- Observabilidade e Monitoramento
- Documentação
- Gestão de Incidentes
- Processos Ágeis e Fluxo

---

*Documento gerado para assessment da Squad Extrato — Ciclo de Desenvolvimento de Software*
