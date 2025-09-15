import pandas as pd
import os

def filter_datas(df: pd.DataFrame) -> pd.DataFrame:
  return df[['Ôxidos', '%', 'Elementos', '%%']]

def save_to_excel(datas_filter: pd.DataFrame,
                  path: str,
                  sheet_name: str = 'Tabela') -> str:
  # Salva o Dataframe
  datas_filter.to_excel(path, index=False, sheet_name=sheet_name)
  return path