# Estudo para certificações Azure

Histórico de estudo e workspace do Cursor. As anotações ficam no Notion; este repo não guarda resumos consultáveis.

## Certificação ativa

- Contexto: [STUDY.md](./STUDY.md)
- Outline AZ-900: [az-900/README.md](./az-900/README.md)

## Progresso


- [Painel](./az-900/progresso/PAINEL.md) — acertos, temas a revisar, projeção
- [Diário de sessões](./az-900/progresso/sessoes.md)
- `az-900/progresso/questoes.csv` — cada item respondido

Atualizar o painel:

```bash
python3 az-900/progresso/painel.py
```

## Estrutura

```text
STUDY.md                 contexto da cert ativa
.cursor/skills/az900-*   skills do agente
az-900/
  README.md              outline da prova
  progresso/             csv, diário, painel
  labs/                  experimentos opcionais
```

## Skills

- `az900-exam-summary` — cheatsheet no chat (Microsoft Learn)
- `az900-practice-questions` — quiz no nível da prova + registro no progresso
- `az900-translation-review` — revisão de tradução do Learn

Outras certificações, quando existirem, repetem a pasta (`az-204/…`) e skills com o prefixo do exame.
