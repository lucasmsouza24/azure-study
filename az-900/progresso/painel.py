#!/usr/bin/env python3
"""Gera PAINEL.md a partir de questoes.csv e do checklist em az-900/README.md."""

import csv
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

BASE = Path(__file__).resolve().parent
CSV_PATH = BASE / "questoes.csv"
README_PATH = BASE.parent / "README.md"
PAINEL_PATH = BASE / "PAINEL.md"

DOMINIOS = {"N": "conceitos da nuvem", "A": "arquitetura", "G": "gerenciamento"}
CHUTE = 0.25
JANELA = 10
NOMES_CONFIANCA = {"C": "Certeza", "D": "Dúvida", "X": "Chute", "?": "Não informada"}
NOMES_FORMATO = {
    "multipla-escolha": "Múltipla escolha",
    "sim-nao": "Sim/Não",
    "completar": "Completar a frase",
    "associacao": "Associação",
    "multipla-selecao": "Múltipla seleção",
}
NOMES_NIVEL = {"essencial": "Essencial", "detalhe": "Detalhe do Learn"}
NOMES_ERRO = {
    "conteudo": "Conteúdo (não sabia)",
    "distracao": "Distração (sabia, mas leu ou marcou errado)",
    "pegadinha": "Pegadinha (caiu no distrator vizinho)",
    "nomenclatura": "Nomenclatura (confundiu nomes)",
}


def carregar_requisitos():
    dominios, requisitos = {}, {}
    atual = None
    contador = Counter()
    for linha in README_PATH.read_text(encoding="utf-8").splitlines():
        if linha.startswith("## "):
            atual = None
            pesos = re.search(r"\((\d+) a (\d+)%\)", linha)
            if pesos:
                for prefixo, chave in DOMINIOS.items():
                    if chave in linha.lower():
                        atual = prefixo
                        dominios[prefixo] = {
                            "nome": re.sub(r"\s*\(.*\)", "", linha[3:]).strip(),
                            "peso": (int(pesos.group(1)) + int(pesos.group(2))) / 2,
                        }
        elif atual and re.match(r"- \[[ x]\] ", linha):
            contador[atual] += 1
            texto = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", linha[6:]).strip()
            requisitos[f"{atual}{contador[atual]:02d}"] = texto
    return dominios, requisitos


def carregar_questoes(requisitos):
    with CSV_PATH.open(encoding="utf-8", newline="") as arquivo:
        linhas = list(csv.DictReader(arquivo))
    invalidas = [l for l in linhas if l["requisito"] not in requisitos]
    for linha in invalidas:
        print(f"Aviso: requisito desconhecido '{linha['requisito']}' ({linha['data']}, {linha['tema']})", file=sys.stderr)
    return [l for l in linhas if l["requisito"] in requisitos]


def certo(linha):
    return linha["resultado"] == "certo"


def pct(valor):
    return "—" if valor is None else f"{100 * valor:.0f}%"


def taxa(linhas):
    return sum(certo(l) for l in linhas) / len(linhas) if linhas else None


def taxa_firme(linhas):
    informadas = [l for l in linhas if l["confianca"] in ("C", "D", "X")]
    if not informadas:
        return None
    return sum(certo(l) and l["confianca"] == "C" for l in informadas) / len(informadas)


def firme(linhas):
    informadas = sum(l["confianca"] in ("C", "D", "X") for l in linhas)
    return f"{pct(taxa_firme(linhas))} de {informadas}" if informadas else "—"


def media(valores):
    valores = [v for v in valores if v is not None]
    return sum(valores) / len(valores) if valores else None


def tabela(cabecalho, linhas):
    saida = ["| " + " | ".join(cabecalho) + " |", "| " + " | ".join("---" for _ in cabecalho) + " |"]
    saida += ["| " + " | ".join(str(c) for c in linha) + " |" for linha in linhas]
    return "\n".join(saida)


def gerar():
    dominios, requisitos = carregar_requisitos()
    questoes = carregar_questoes(requisitos)

    por_requisito = defaultdict(list)
    for linha in questoes:
        por_requisito[linha["requisito"]].append(linha)
    recentes = {r: linhas[-JANELA:] for r, linhas in por_requisito.items()}

    resumo_dominios, proj_estudado, proj_hoje = [], [], []
    for prefixo, info in dominios.items():
        ids = [r for r in requisitos if r.startswith(prefixo)]
        estudados = [r for r in ids if r in por_requisito]
        linhas = [l for r in estudados for l in por_requisito[r]]
        acerto_estudado = media(taxa(recentes[r]) for r in estudados)
        acerto_hoje = media(taxa(recentes[r]) if r in recentes else CHUTE for r in ids)
        if acerto_estudado is not None:
            proj_estudado.append((info["peso"], acerto_estudado))
        proj_hoje.append((info["peso"], acerto_hoje))
        resumo_dominios.append([
            info["nome"], f"{info['peso']:.1f}%", f"{len(estudados)}/{len(ids)}",
            len(linhas), pct(taxa(linhas)), firme(linhas),
        ])

    def ponderada(pares):
        return sum(p * v for p, v in pares) / sum(p for p, _ in pares) if pares else None

    total = len(questoes)
    erros = [l for l in questoes if not certo(l)]
    falsa_certeza = [l for l in erros if l["confianca"] == "C"]

    partes = [
        "# Painel de progresso AZ-900",
        "",
        "Gerado por `painel.py` a partir de `questoes.csv`. Não edite à mão: rode `python3 az-900/progresso/painel.py`.",
        "",
        "## Resumo",
        "",
        tabela(["Indicador", "Valor"], [
            ["Itens respondidos", total],
            ["Sessões", len({l["sessao"] for l in questoes})],
            ["Acerto geral", pct(taxa(questoes))],
            ["Acerto firme (certo com certeza, entre itens com confiança informada)", pct(taxa_firme(questoes))],
            ["Erros com certeza (falsa certeza)", len(falsa_certeza)],
        ]),
        "",
        "## Projeção",
        "",
        tabela(["Cenário", "Acerto ponderado"], [
            ["Conteúdo já estudado (média dos requisitos estudados, ponderada pelo peso do domínio)", pct(ponderada(proj_estudado))],
            [f"Se a prova fosse hoje (requisitos não estudados contam como chute, {CHUTE:.0%})", pct(ponderada(proj_hoje))],
        ]),
        "",
        f"Cada requisito conta igual dentro do domínio e usa só as {JANELA} tentativas mais recentes. "
        "A Microsoft usa uma escala de 1 a 1000, com aprovação em 700, e não divulga a conversão a partir do número de acertos. "
        "Como referência prática, mire em mais de 80% no conteúdo estudado.",
        "",
        "## Por domínio",
        "",
        tabela(["Domínio", "Peso", "Requisitos estudados", "Itens", "Acerto", "Firme"], resumo_dominios),
        "",
        "## Por requisito",
        "",
        tabela(["ID", "Requisito", "Itens", f"Acerto (últimos {JANELA})", "Firme", "Última vez"], [
            [r, requisitos[r], len(por_requisito[r]), pct(taxa(recentes[r])), firme(por_requisito[r]), por_requisito[r][-1]["data"]]
            for r in requisitos if r in por_requisito
        ]),
        "",
        "Firme = acertou com certeza, entre os itens em que a confiança foi informada (o número indica quantos).",
    ]

    def agrupado(campo, titulo, rotulos=None):
        grupos = defaultdict(list)
        for linha in questoes:
            grupos[linha[campo] or "—"].append(linha)
        chaves = rotulos.keys() if rotulos else sorted(grupos)
        linhas = [[(rotulos or {}).get(c, c), len(grupos[c]), pct(taxa(grupos[c]))] for c in chaves if c in grupos]
        return ["", f"## {titulo}", "", tabela([titulo.split(" por ")[-1].capitalize(), "Itens", "Acerto"], linhas)]

    partes += agrupado("formato", "Acerto por formato", NOMES_FORMATO)
    partes += agrupado("nivel", "Acerto por nível", NOMES_NIVEL)
    partes += agrupado("confianca", "Acerto por confiança", NOMES_CONFIANCA)

    tipos = Counter(l["erro"] or "não classificado" for l in erros)
    partes += ["", "## Tipos de erro", ""]
    partes.append(tabela(["Tipo", "Erros"], [[NOMES_ERRO.get(t, t), n] for t, n in tipos.most_common()]) if tipos else "Nenhum erro registrado.")

    ultimo_por_tema, teve_erro = {}, set()
    for linha in questoes:
        chave = (linha["requisito"], linha["tema"])
        ultimo_por_tema[chave] = linha
        if not certo(linha):
            teve_erro.add(chave)

    revisar = [(c, l) for c, l in ultimo_por_tema.items() if not certo(l)]
    frageis = [(c, l) for c, l in ultimo_por_tema.items() if certo(l) and l["confianca"] in ("D", "X")]
    recuperados = [(c, l) for c, l in ultimo_por_tema.items() if c in teve_erro and certo(l) and l["confianca"] not in ("D", "X")]

    def lista_temas(itens):
        if not itens:
            return "Nenhum."
        return tabela(["Requisito", "Tema", "Última vez", "Observação"], [
            [c[0], c[1], l["data"], l["obs"] or "—"] for c, l in sorted(itens)
        ])

    partes += [
        "", "## Temas a revisar (última tentativa errada)", "", lista_temas(revisar),
        "", "## Temas frágeis (última tentativa certa com dúvida ou chute)", "", lista_temas(frageis),
        "", "## Temas recuperados (já errou, mas acertou depois)", "", lista_temas(recuperados),
        "",
    ]

    PAINEL_PATH.write_text("\n".join(partes), encoding="utf-8")
    print(f"{PAINEL_PATH.relative_to(BASE.parent.parent)} atualizado: {total} itens, "
          f"acerto {pct(taxa(questoes))}, projeção do estudado {pct(ponderada(proj_estudado))}, "
          f"projeção hoje {pct(ponderada(proj_hoje))}")


if __name__ == "__main__":
    gerar()
