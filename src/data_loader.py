import pandas as pd

def load_excel(path: str, header: int = 17, nrows: int = 15) -> pd.DataFrame:
  return pd.read_excel(path, sheet_name=0, header=header-1, nrows=nrows)