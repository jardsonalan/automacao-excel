import pandas as pd

def filter_datas(df: pd.DataFrame) -> pd.DataFrame:
  return df[['Ôxidos', '%', 'Elementos', '%%']]

def save_to_excel(name: str, datas_filter: pd.DataFrame, sheet_name="Table") -> str:
  datas_filter.to_excel('./data/processed/'+name+'.xlsx', index=False, sheet_name=sheet_name)
  return 'Nova tabela criada.'