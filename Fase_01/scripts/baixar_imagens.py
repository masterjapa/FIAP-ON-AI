"""
CardioIA - Fase 1 | Parte 3: download da amostra de imagens de ECG.

Baixa direto da API publica do Mendeley Data uma amostra balanceada por classe.
A base completa (v2) tem 928 ECGs e ~615 MB; o enunciado pede no minimo 100
imagens, entao baixamos so o recorte necessario.

A classe de cada exame esta no prefixo do nome do arquivo:
  Normal = pessoa normal | HB = batimento anormal
  MI     = infarto agudo | PMI = historico previo de infarto

Uso:
  python baixar_imagens.py --por-classe 32

Fonte  : ECG Images dataset of Cardiac Patients (DOI 10.17632/gwbz3fsgp8.2)
Licenca: CC BY 4.0
"""

import argparse
import json
import re
from collections import defaultdict
from pathlib import Path
from urllib.request import Request, urlopen

API = "https://data.mendeley.com/public-api/datasets/gwbz3fsgp8"

CLASSES = {
    "Normal": "01_normal",
    "HB": "02_batimento_anormal",
    "MI": "03_infarto_agudo",
    "PMI": "04_historico_infarto",
}


def buscar(url: str) -> bytes:
    pedido = Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urlopen(pedido) as resposta:
        return resposta.read()


def listar_por_classe() -> dict:
    arquivos = json.loads(buscar(API))["files"]
    grupos = defaultdict(list)
    for arquivo in arquivos:
        prefixo = re.match(r"[A-Za-z]+", arquivo["filename"]).group(0)
        if prefixo in CLASSES:
            grupos[prefixo].append(arquivo)
    # Ordem alfabetica em vez de sorteio: a amostra fica reproduzivel.
    return {k: sorted(v, key=lambda a: a["filename"]) for k, v in grupos.items()}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--por-classe", type=int, default=32,
                        help="imagens por classe (padrao: 32, total 128)")
    parser.add_argument("--destino", type=Path,
                        default=Path(__file__).resolve().parent.parent / "imagens_ecg")
    args = parser.parse_args()

    grupos = listar_por_classe()
    total = 0
    for prefixo, pasta_nome in CLASSES.items():
        selecionadas = grupos[prefixo][:args.por_classe]
        pasta = args.destino / pasta_nome
        pasta.mkdir(parents=True, exist_ok=True)
        for arquivo in selecionadas:
            destino = pasta / arquivo["filename"]
            if not destino.exists():
                destino.write_bytes(buscar(arquivo["content_details"]["download_url"]))
        total += len(selecionadas)
        print("{:<24} {:>3} de {:>4} disponiveis".format(
            pasta_nome, len(selecionadas), len(grupos[prefixo])))

    print("\nTotal: {} imagens em {}".format(total, args.destino))
    if total < 100:
        print("ATENCAO: o enunciado pede no minimo 100 imagens. Aumente --por-classe.")


if __name__ == "__main__":
    main()
