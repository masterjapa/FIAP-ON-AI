"""
CardioIA - Fase 1 | Parte 2: preparacao dos textos para NLP.

Baixa os dois artigos em PDF do SciELO e converte para .txt UTF-8 em assets/.
Cada arquivo recebe um cabecalho com titulo, fonte, DOI e licenca, para que a
procedencia viaje junto com o texto.
"""

from pathlib import Path
from urllib.request import Request, urlopen
import io

from pypdf import PdfReader

ASSETS = Path(__file__).resolve().parent.parent / "assets"

TEXTOS = [
    {
        "arquivo": "texto_01_estatistica_cardiovascular_brasil_2023.txt",
        "titulo": "Estatistica Cardiovascular - Brasil 2023",
        "fonte": "Arquivos Brasileiros de Cardiologia, v. 121, n. 2, 2024",
        "doi": "10.36660/abc.20240079",
        "licenca": "Open Access (SciELO)",
        "url": "https://www.scielo.br/j/abc/a/jzFMcdN5y3w6CtjVgdJdSdR/?format=pdf&lang=pt",
    },
    {
        "arquivo": "texto_02_fatores_risco_cardiovascular.txt",
        "titulo": (
            "Frequencia de fatores de risco cardiovascular em voluntarios "
            "participantes de evento de educacao em saude"
        ),
        "fonte": "Revista da Associacao Medica Brasileira, v. 55, n. 5, 2009",
        "doi": "10.1590/S0104-42302009000500028",
        "licenca": "CC BY 4.0",
        "url": "https://www.scielo.br/j/ramb/a/yVZZhHcT59Dvr8f9LzqZhZz/?format=pdf&lang=pt",
    },
]


def baixar_pdf(url: str) -> bytes:
    # O SciELO recusa requisicoes sem User-Agent de navegador.
    pedido = Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urlopen(pedido) as resposta:
        return resposta.read()


def extrair(pdf: bytes) -> str:
    leitor = PdfReader(io.BytesIO(pdf))
    return "\n\n".join(pagina.extract_text() or "" for pagina in leitor.pages)


def cabecalho(meta: dict) -> str:
    return (
        "Titulo : {titulo}\n"
        "Fonte  : {fonte}\n"
        "DOI    : https://doi.org/{doi}\n"
        "Licenca: {licenca}\n"
        "{regua}\n\n"
    ).format(regua="-" * 70, **meta)


def main() -> None:
    ASSETS.mkdir(parents=True, exist_ok=True)
    for meta in TEXTOS:
        texto = extrair(baixar_pdf(meta["url"]))
        destino = ASSETS / meta["arquivo"]
        destino.write_text(cabecalho(meta) + texto, encoding="utf-8")
        print("{}  ({} caracteres, {} palavras)".format(
            meta["arquivo"], len(texto), len(texto.split())
        ))


if __name__ == "__main__":
    main()
