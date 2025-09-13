import pandas as pd

def load_excel(path: str, header=16, nrows=15) -> pd.DataFrame:
  return pd.read_excel(path, sheet_name=0, header=header, nrows=nrows)