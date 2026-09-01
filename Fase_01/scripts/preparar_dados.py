"""
CardioIA - Fase 1 | Parte 1: preparacao do dataset numerico.

Baixa a base Cleveland do UCI Heart Disease, aplica os nomes de coluna do
dicionario oficial, marca os valores ausentes e grava dados/cardioia_pacientes.csv.

Fonte : https://archive.ics.uci.edu/dataset/45/heart+disease
Licenca: CC BY 4.0
"""

from pathlib import Path
from urllib.request import urlopen

import pandas as pd

URL = "https://archive.ics.uci.edu/static/public/45/data.csv"
SAIDA = Path(__file__).resolve().parent.parent / "dados" / "cardioia_pacientes.csv"

# 14 variaveis do subconjunto usado pela literatura, na ordem do dicionario do UCI.
COLUNAS = [
    "age", "sex", "cp", "trestbps", "chol", "fbs", "restecg",
    "thalach", "exang", "oldpeak", "slope", "ca", "thal", "num",
]


def baixar() -> pd.DataFrame:
    """Le a base direto do UCI. O '?' do arquivo original vira NaN."""
    with urlopen(URL) as resposta:
        return pd.read_csv(resposta, na_values="?")


def preparar(df: pd.DataFrame) -> pd.DataFrame:
    df = df[COLUNAS].copy()
    # 'num' vai de 0 (sem doenca) a 4 (grau de obstrucao). A literatura do dataset
    # trabalha com o problema binario: presenca versus ausencia de doenca.
    df["doenca_cardiaca"] = (df["num"] > 0).astype(int)
    return df


def main() -> None:
    df = preparar(baixar())
    SAIDA.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(SAIDA, index=False)

    print("Arquivo gravado: {}".format(SAIDA))
    print("Registros: {} | Colunas: {}".format(len(df), len(df.columns)))
    print("\nValores ausentes:")
    ausentes = df.isna().sum()
    print(ausentes[ausentes > 0].to_string() or "  nenhum")
    print("\nDistribuicao do alvo (0 = sem doenca, 1 = com doenca):")
    print(df["doenca_cardiaca"].value_counts().sort_index().to_string())


if __name__ == "__main__":
    main()
