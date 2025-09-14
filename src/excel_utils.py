import pandas as pd
import os

def filter_datas(df: pd.DataFrame) -> pd.DataFrame:
  return df[['Ôxidos', '%', 'Elementos', '%%']]

def save_to_excel(datas_filter: pd.DataFrame,
                  name: str,
                  folder: str = './data/processed',
                  sheet_name: str = 'Tabela') -> str:
  
  # Serve para garantir que a pasta (folder) existe
  os.makedirs(folder, exist_ok=True)

  # Garante a extensão (.xlsx)
  if not name.endswith('.xlsx'):
    name += '.xlsx'
  
  path = os.path.join(folder, name)

  # Salva o Dataframe
  datas_filter.to_excel(path, index=False, sheet_name=sheet_name)

  return path