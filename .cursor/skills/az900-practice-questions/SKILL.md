---
name: az900-practice-questions
description: Gera questões no estilo AZ-900 (cenário, escolha de serviço, definição) com gabarito e justificativa em PT-BR e termos EN. Use when the user asks for practice questions, quiz, simulado, flashcards, or to test a topic.
---

# AZ-900 practice questions

Gere itens no estilo **Microsoft AZ-900 (Fundamentals)**: reconhecimento de conceito/serviço, **dificuldade alinhada à prova real** (não “quiz fácil de eliminação”).

## Antes de gerar

1. Confirme o tópico (ou sorteie pelo outline em `az-900/README.md` se o pedido for amplo).
2. Respeite `STUDY.md`: pode **enfatizar** governança, mas não monte um quiz só disso salvo pedido. Misture os três domínios quando o tema for “me testa”.
3. Padrão: **5 questões** se ele não pedir quantidade. Misture tipos.
4. Calibre pela seção **Nível de dificuldade (padrão = prova)** abaixo — a menos que ele peça “mais fácil” / “revisão leve”.
5. Se o set for de um tema principal (estudo ou revisão), prepare **1–2 itens de bônus** pela seção **Bônus de revisão (repetição espaçada)** abaixo — consulte `PAINEL.md` e a data da última visita em `questoes.csv`.

## Bônus de revisão (repetição espaçada)

Objetivo: 1–2 questões no fim do set, de temas **não relacionados** ao tema principal da rodada, para reforçar retenção.

### Prioridade de escolha (nessa ordem)

1. **Temas a revisar** e **Temas frágeis** do `PAINEL.md` (erro recente ou acerto com dúvida/chute).
2. **Requisitos ou temas com dificuldade histórica** (já errou antes; preferir o aspecto específico frágil — ex. site a site vs ponto a site, não “rede” genérico).
3. **Mais tempo sem visitar**: entre requisitos já estudados, pegue os de **última data mais antiga** em `questoes.csv` / coluna “Última vez” do `PAINEL.md` (conceitos de nuvem e arquitetura antiga costumam cair aqui).

### Não fazer

- Bônus do **mesmo requisito** (ou vizinho imediato) que a rodada principal acabou de cobrir ou cobriu na rodada anterior da mesma sessão.
- Repetir o mesmo bônus em sessões seguidas se já foi recuperado com certeza.
- Inventar tema não estudado ainda só para “preencher” o bônus.

### Formato do bônus

Mesmo nível prova; pode ser 1 escolha única ou 1 Sim/Não curto. Rotule como **Bônus de revisão** e cite o requisito/tema em uma palavra (ex. “rede — VPN site a site”).

## Nível de dificuldade (padrão atual = exigente)

A AZ-900 **não** exige design profundo, mas também **não** deve cair por absurdo óbvio. O desafio típico é **distrator vizinho** + enunciado com 1–2 pistas.

Desde 20/10/2026 o Lucas está na **fase de revisão**: o padrão de todas as rodadas (inclusive bônus e temas recém-estudados) é o **nível exigente** abaixo, sem aumentar a quantidade de questões. O nível prova vale só se ele pedir "mais fácil" ou "revisão leve".

### Nível exigente (padrão na fase de revisão)

Tudo do nível prova, mais:

- **Cenários com mais de uma restrição**, em que só a alternativa certa atende a todas (ex.: "demanda imprevisível **e** sem compra antecipada **e** gasto que cai com o uso").
- **Alternativas compostas** que exigem acertar duas coisas ao mesmo tempo (ex.: o modelo **e** a classificação CapEx/OpEx; o pilar **e** a capacidade).
- Distratores **só vizinhos**, incluindo um que pareça certo por um detalhe do enunciado (ex.: VM spot "barata" quando o tráfego é crítico).
- **Armadilhas de leitura** de forma deliberada, nunca por ambiguidade: verbo que não corresponde ao conceito, nome de produto que puxa para o vizinho, "só"/"sempre"/"nunca" mudando o sentido.
- Afirmações de Sim/Não que exigem o detalhe certo do Learn, não a ideia geral.

Limites: nada fora do Learn; nenhuma questão em que duas alternativas possam ser defendidas. Se uma armadilha depende de uma palavra que o Learn usa em dois sentidos, reescreva até ficar sem ambiguidade. A exigência vem do **cenário**, não de rótulos secundários: não monte o set em torno de uma nomenclatura menor da unidade (ex.: "gerenciamento da nuvem" vs "na nuvem"); isso continua contando como detalhe do Learn, no máximo 1 a cada 5.

### Faça (nível prova)

- Distratores do **mesmo cluster** do tópico (ex. rede: VNet, subnet, peering, VPN Gateway, ExpressRoute, NSG, Azure DNS — não “Front Door” nem “availability set” só para preencher).
- Cenários curtos com **uma** diferença decisiva (ex. “pela Internet criptografada” vs “conexão privada / sem Internet pública”).
- Linguagem de prova: “mais adequado”, “melhor atende”, “qual afirmação é verdadeira”.
- Pelo menos **3 de 5** questões do set devem exigir distinguir **pares clássicos** (lista abaixo), não só definir o termo isolado.
- Enunciado pode ter 2–4 frases; a pista certa deve estar no texto, sem ser gritada.

### Evite (fica mais fácil que a prova)

- Alternativa “de outro universo” que qualquer um elimina sem saber o tema (ex. resource lock em pergunta de peering; ExpressRoute em pergunta de App Service — salvo o set ser misto multi-domínio e o distrator ainda for plausível no enunciado).
- Definição literal copiada + 3 opções ridículas.
- Perguntas que só testam “VNet = rede” sem nenhum vizinho confuso.
- Jargão de AZ-104/700 (SKU detalhado, CIDR, config de portal/CLI, preview).

### Pares / clusters de pegadinha (use com frequência)

| Cluster | Confusões típicas |
| --- | --- |
| Rede | peering vs VPN S2S vs ExpressRoute; subnet vs VNet; Azure DNS hospeda ≠ compra domínio; VPN route-based vs policy-based (só o essencial do Learn) |
| Computação | VM vs App Service vs Functions vs containers; VMSS vs availability set |
| Arquitetura | region vs region pair vs AZ; CapEx vs OpEx |
| Governança | MG vs SUB vs RG; RBAC vs Policy vs resource lock; role vs service principal |
| Identidade | authentication vs authorization; MFA vs Conditional Access (nível describe) |

### Profundidade do conteúdo (o que a prova cobra)

Dificuldade vem do **distrator vizinho**, não de detalhe obscuro. Classifique cada questão antes de entregar:

| Nível | O que é | Peso no set |
| --- | --- | --- |
| **Essencial** | Finalidade do serviço/conceito e como diferenciá-lo dos vizinhos (“qual usar”) | Maioria — pelo menos 4 de 5 (ou 8 de 10) |
| **Detalhe do Learn** | Funcionalidade secundária citada **explicitamente** no texto da unidade do Learn (ex.: zonas DNS privadas, VPN baseada em rota, Global Reach). Priorize as que aparecem na avaliação do módulo (`knowledge check`) | No máximo 1 por 5 questões |
| **Fora do escopo** | Qualquer coisa que não esteja na unidade do Learn do requisito (SKU, CIDR, configuração, limites numéricos) | Nunca |

Em questão de **detalhe do Learn**, o enunciado deve trazer a pista que permite resolver por raciocínio (ex.: “recomendado”, “mais flexível”), e o gabarito deve marcar `Nível: detalhe do Learn`.

### Se ele pedir outro nível

- **“mais fácil” / revisão leve:** volte ao nível prova; pode usar 1–2 distratores mais distantes e mais definições diretas.
- **“mais difícil”:** além do nível exigente, alongue o cenário; nunca invente conteúdo fora do outline AZ-900.

## Tipos (varie)

- Definição direta (“o que é X”) — no máximo ~1–2 por set de 5 no modo prova
- Cenário (“qual serviço / modelo atende”) — maioria
- Comparação (“qual afirmação é verdadeira”)
- Hierarquia / responsabilidade (MG, SUB, RG, resource, RBAC vs Policy)

Evite: passos de CLI, nomes de SKU, valores de preço, features preview.

## Formatos da prova real (padrão: sempre misturar)

**Todo set** mistura formatos. Rótulos no chat (o que o Lucas lê) ≠ códigos do CSV (compatibilidade do painel).

| Rótulo no chat | Significado | Código em `questoes.csv` | Como ele responde |
| --- | --- | --- | --- |
| **Escolha única** | Uma resposta certa entre A–D | `multipla-escolha` | `1B` |
| **Sim/Não** | Bloco de 3 afirmações; cada uma Sim ou Não | `sim-nao` | `2: N/S/N` |
| **Completar a frase** | Lacuna + opções | `completar` | `3B` |
| **Associação** | 3–4 cenários ↔ opções (arrastar e soltar) | `associacao` | `4: 1C, 2A, 3D, 4B` |
| **Múltipla escolha** | Mais de uma correta (“escolha duas/três”) entre A–E | `multipla-selecao` | `5: BD` |

Não chame de “múltipla escolha” a questão de **uma** alternativa correta — use **escolha única**. “Múltipla escolha” fica só para marcar várias.

Composição de referência para ~6 itens:

- 2–3 de **escolha única**
- 1 bloco de **Sim/Não**
- 1–2 entre **completar**, **associação** e **múltipla escolha**, alternando entre rodadas

Em sets curtos (3–4), pelo menos 2 formatos. Formato único só se ele pedir.

**Legibilidade das alternativas:** cada A/B/C… e cada item de associação em **item de lista próprio** (`- **A.** texto`), nunca linhas soltas.

Para calibrar com a prova real: a Microsoft oferece avaliação prática gratuita na página da certificação; recomende quando ele perguntar.

## Variabilidade e anti-padrões (obrigatório antes de entregar)

Não sacrifique qualidade do conteúdo — só a **posição** das certas e o **padrão** de Sim/Não.

### Sim/Não (3 afirmações)

- **Proibido** como padrão default: `S/N/S` (foi o padrão repetido demais).
- Conte Sim e Não: não deixe quase sempre 2 Sim + 1 Não. Alterne quantidades: 2N+1S, 2S+1N, 3S, 3N (raro), ou 1S+2N.
- Embaralhe a **ordem** das afirmações (a verdadeira/falsa não fica sempre no meio).
- Antes de enviar, escreva o gabarito do bloco (ex. `N/N/S`). Se for `S/N/S` e a rodada anterior também foi, **remisture** afirmações ou reescreva uma.
- Exemplos válidos: `N/S/N`, `S/S/N`, `N/N/S`, `S/N/N`, `N/S/S`, `S/S/S` (só se as três forem realmente verdadeiras).

### Escolha única e completar

- Espalhe A/B/C/D: em set de 5+, **pelo menos 3 letras diferentes** nas respostas certas.
- Não deixe a correta “sempre no meio” (B/C). Embaralhe de propósito.
- Se 4+ itens de escolha única/completar caírem nas mesmas 2 letras, remisture.

### Múltipla escolha (“escolha duas/três”)

- **Proibido** como default: gabarito sempre `A,B` / `AB`.
- Varie pares/trios: `A,C`, `B,D`, `C,E`, `A,D`, `B,C`, `A,B,D`, `B,C,E`, etc.
- As opções corretas devem ser as que o conteúdo exige; se o conteúdo der AB, **troque a ordem das alternativas** (embaralhe A–E) para o gabarito deixar de ser AB, sem mudar o que está certo.
- No enunciado: “Escolha duas” / “Escolha três” — nunca “escolha todas” sem número, salvo o Learn exigir.

### Associação

- Cada opção uma vez (salvo aviso). Ordem das opções **≠** ordem dos cenários (nada de 1A, 2B, 3C, 4D).
- Embaralhe o gabarito entre rodadas (não sempre 1C,2A,3D,4B).

### Checklist rápido (mental, antes de enviar)

1. Rótulos: escolha única vs múltipla escolha corretos?
2. Sim/Não ≠ `S/N/S` se a última rodada já foi isso?
3. Múltipla escolha ≠ sempre `AB`?
4. Letras das escolhas únicas espalhadas?
5. Distratores ainda vizinhos e corretos no Learn?

## Formato

Mostre **todas as perguntas primeiro**, depois o gabarito — para ele tentar sozinho.

```markdown
### Questões

**1.** [enunciado em PT-BR; termos-chave também em inglês na primeira vez]
- A. ...
- B. ...
- C. ...
- D. ...

### Gabarito

**1. [letra] — [resposta curta]**
- Por quê: 2–4 linhas no nível da prova
- Termo EN: `...`
- Pegadinha: por que a alternativa X parece certa e não é
- Nível: essencial | detalhe do Learn
```

No gabarito, a **Pegadinha** deve citar o distrator **mais tentador** (o vizinho), não só o absurdo.

## Qualidade dos distratores (checklist antes de entregar)

Para cada questão:

1. A certa está correta no recorte Learn/AZ-900.
2. Cada errada é um **conceito Azure real** que alguém confunde com a certa.
3. Um aluno que só “chuta por eliminação grosseira” **não** deveria acertar com facilidade — precisa da pista do enunciado.
4. Nenhuma alternativa é humor/absurdo (“desligar a Internet”, “comprar cabo USB”, etc.).

## Registro de progresso (obrigatório após corrigir)

Depois de corrigir as respostas dele, registre a rodada em `az-900/progresso/`:

1. **`questoes.csv`:** acrescente ao final uma linha por **item pontuável** (cada afirmação de Sim/Não, cada par de associação, cada escolha única, completar ou múltipla escolha). Colunas:
   - `data` (AAAA-MM-DD) e `sessao` (`S01`, `S02`…; uma sessão por dia, continuando a numeração de `sessoes.md`)
   - `requisito`: ID do item do checklist em `az-900/README.md`, numerado por domínio na ordem do arquivo (`N01`–`N15` nuvem, `A01`–`A27` arquitetura, `G01`–`G15` governança)
   - `tema`: conceito curto e **estável** (reuse o mesmo texto de rodadas anteriores para o mesmo conceito, para o painel detectar recuperação)
   - `formato`: `multipla-escolha` (= escolha única no chat), `sim-nao`, `completar`, `associacao` ou `multipla-selecao` (= múltipla escolha no chat). **Não renomeie** os códigos do CSV — o painel histórico depende deles.
   - `nivel`: `essencial` ou `detalhe`
   - `resultado`: `certo` ou `errado`
   - `confianca`: `C`, `D`, `X` ou `?` (não informada)
   - `erro` (só se errou): `conteudo`, `distracao`, `pegadinha` ou `nomenclatura`
   - `obs`: detalhe curto, sem vírgulas
2. **`sessoes.md`:** crie ou atualize a entrada da sessão do dia com o que foi estudado, placar de cada rodada, erros relevantes, decisões e próximo passo.
3. Rode `python3 az-900/progresso/painel.py` e cite em uma linha a mudança relevante (projeção, tema que entrou ou saiu da lista de revisão).

Registre também em `sessoes.md` os temas estudados por resumo, mesmo sem quiz.
