---
name: az900-exam-summary
description: Gera um cheatsheet enxuto de um requisito da AZ-900 (tabelas, listas, termos PT/EN) a partir do Microsoft Learn mais recente, no recorte da prova. Nunca usa Notion como fonte. Use when the user asks for a resumo, cheatsheet, fácil de consultar, or recap and names an exam skill/requirement from the AZ-900 outline.
---

# AZ-900 exam summary

Cheatsheet para **como cai na prova**. Não é artigo e não é cópia das notas do Lucas.

## Gatilho

Pedido do tipo “resumo / cheatsheet / fácil de consultar” + nome do requisito (texto de `az-900/README.md` ou do [guia AZ-900](https://learn.microsoft.com/pt-br/credentials/certifications/resources/study-guides/az-900)).

## Fonte (regra dura)

**Nunca** usar Notion nem MCP Notion neste fluxo — mesmo que exista página do tópico.

Consultar o **Microsoft Learn mais recente** (WebSearch + WebFetch; não recitar de memória se der para abrir a página):

1. Guia de estudo AZ-900 — casar o nome do requisito
2. Unidade do módulo de treino correspondente (PT-BR; cruzar EN-US se o PT parecer genérico ou desatualizado)
3. Avaliação / `knowledge check` do módulo, se existir — pistas de enunciado

No topo da resposta: uma linha **Fonte:** com o link do Learn usado.

Notion só entra se, **depois**, o Lucas pedir para comparar com as notas.

## Formato

Proibir parágrafo longo. Preferir tabela, lista e bullets. Omitir seção vazia; adaptar colunas ao tópico.

```markdown
Fonte: [título](url do Learn)

## [Requisito] (`English name`)

**Na prova:** 1 frase (definir / comparar / escolher o serviço certo).

| … | Use quando / pista no enunciado | Não confundir com |
| --- | --- | --- |

### Cheatsheet
- 3–5 bullets de 1 linha

### Pegadinhas
- Alternativa tentadora vs. resposta certa

### Termos PT ↔ EN
| PT-BR | English |
| --- | --- |
```

Hierarquia/acesso (MG, SUB, RG, resource, role, RBAC, service principal): a tabela principal **é** o contraste desses termos.

## Regras extras

- PT-BR no texto; nome EN na primeira menção e nas tabelas.
- Separe a profundidade: **essencial** (finalidade e diferença entre vizinhos — dominar) vs **detalhe do Learn** (funcionalidades secundárias citadas na unidade — 1 linha cada, só reconhecer). Não inclua o que não está no Learn.
- Sem portal, SKU, CLI, preço — salvo o outline pedir.
- `STUDY.md` só calibra profundidade (governança = mais contraste), não é fonte de conteúdo.
