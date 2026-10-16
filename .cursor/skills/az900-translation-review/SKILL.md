---
name: az900-translation-review
description: Revisa tradução PT-BR da documentação Microsoft Learn / AZ-900, checa termos oficiais e o equivalente em inglês para a prova. Use when the user pastes docs, asks to evaluate a translation, compare EN vs PT, or check terminology.
---

# AZ-900 translation review

Avalie o trecho **como material de prova**, não como revisão literária.

## Entrada

Aceite: colagem EN, colagem PT, ou os dois. Se só vier um idioma, infira o par oficial (Microsoft Learn PT-BR ↔ EN-US).

## Formato

```markdown
## Veredito
1–2 frases: a tradução está alinhada à prova? Há risco de confusão de termo?

## Termos
| No texto | Oficial PT-BR | English (prova / trabalho) | Risco |
| --- | --- | --- | --- |

## Trechos
Para cada problema:
- **Original**
- **Sugestão** (Learn PT-BR + `English`)
- **Por que importa na AZ-900** (1 linha)

## O que está ok
Lista curta — não reescreva o que já está certo.
```

## Critérios

- Priorize consistência com [Microsoft Learn PT-BR](https://learn.microsoft.com/pt-br/) e nomes de produto **não traduzidos**.
- Sinalize quando o PT-BR oficial diverge do jargão de trabalho (ex.: grupo de recursos vs `resource group` / RG).
- Não “melhore o estilo” da Microsoft; só aponte ambiguidade, termo errado ou tradução que muda o conceito (shared responsibility, lock, policy, subscription).
- Se um termo tiver duas traduções aceitáveis, diga qual a prova costuma usar e mantenha o EN ao lado.
