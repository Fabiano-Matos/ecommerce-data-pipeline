from pathlib import Path
import pandas as pd

# caminho base do projeto
BASE_DIR = Path(__file__).resolve().parents[2]

# caminho do arquivo de dados
DATA_PATH = BASE_DIR / "data" / "raw" / "ecommerce_10000.csv"


def extract_data(file_path: Path) -> pd.DataFrame:
    df = pd.read_csv(file_path)
    return df


def main():
    df = extract_data(DATA_PATH)

    print(df.head())
    
    print("\nInformações do dataset:")
    print(df.info())
    
    print("nEstatisticas numéricas:")
    print(df.describe())

    print("nValores nulospor coluna:")
    print(df.isnull().sum())



    print(f"\nTotal de linhas: {df.shape[0]}")
    print(f"Total de colunas: {df.shape[1]}")


if __name__ == "__main__":
    main()