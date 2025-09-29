import pandas as pd

def rename_headers(df: pd.DataFrame) -> pd.DataFrame:
  return df.rename(columns={
    'Compound': 'Óxidos',
    'm/m%': '%',
    'm/m%.1': '%%',
    'El': 'Elementos'
  })

def correction_datas(df: pd.DataFrame) -> pd.DataFrame:
  if 'Elementos' in df.columns:
    df['Elementos'] = df['Elementos'].str.strip().replace({
      'Sx': 'S',
      'Px': 'P'
    })

  return df