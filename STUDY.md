# Contexto de estudo

Fonte das anotações: **Notion**. Este repo guarda o histórico de progresso, o contexto do agente e labs opcionais. Resumos saem no chat para colar no Notion; não viram arquivo aqui.

## Meta

- Certificação atual: **AZ-900** (Azure Fundamentals)
- Data da prova: ainda sem data marcada; objetivo **antes do fim de agosto/2026**
- Outline: [az-900/README.md](./az-900/README.md)
- Progresso: [az-900/progresso/PAINEL.md](./az-900/progresso/PAINEL.md) (acertos, temas a revisar e projeção) e [sessoes.md](./az-900/progresso/sessoes.md) (diário)

## Nível por domínio

Não negligenciar nenhum domínio. A prova cobra os três; o comentário abaixo é só familiaridade, não prioridade exclusiva.

| Domínio | Peso | Nível | Nota |
| --- | --- | --- | --- |
| Conceitos da nuvem | 25–30% | Bom | Base ok |
| Arquitetura e serviços | 35–40% | Ok | Precisa **revisar** (maior peso da prova) |
| Gerenciamento e governança | 30–35% | Fraco | Confusão no trabalho; estudar com mais contraste de termos |

## Ponto fraco (governança / hierarquia)

No trabalho os nomes aparecem em inglês/abreviação. Na prova e no Learn, misturam PT e EN. Sempre contrastar:

| Abrev. / jargão | PT-BR | English |
| --- | --- | --- |
| MG | grupo de gerenciamento | management group |
| SUB | assinatura | subscription |
| RG | grupo de recursos | resource group |
| — | recurso | resource |
| SP | entidade de serviço / principal de serviço | service principal |
| role | função | role |
| RBAC | controle de acesso baseado em função | role-based access control |
| — | Azure Policy | Azure Policy |
| lock | bloqueio de recurso | resource lock |

Hierarquia típica: **management group → subscription → resource group → resource**.

Não misturar: **RBAC** (quem pode fazer o quê) vs **Azure Policy** (o que pode ser implantado / conformidade) vs **resource lock** (impede delete/alteração).

## Como usar este workspace

- Tirar dúvidas, revisar tradução do Learn, resumir no nível da prova (no chat), gerar questões
- Anotações vivas no Notion; o histórico fica em `az-900/progresso/`
- Skills: `az900-exam-summary`, `az900-practice-questions`, `az900-translation-review`
- Labs práticos, se houver, em `az-900/labs/`
