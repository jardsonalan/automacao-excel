from data_loader import load_excel
from data_cleaner import rename_headers, correction_datas
from excel_utils import filter_datas, save_to_excel
from excel_formatter import format_excel

def main():
  input_path = './data/raw/AL-E2.xls'
  # Carrega a planilha
  df = load_excel(input_path)
  # Renomeia o cabeçalho
  df = rename_headers(df)
  # Corrije os dados errados
  df = correction_datas(df)
  # Filtra os dados necessários
  df = filter_datas(df)
  # Salva em Excel, após o tratamento dos dados (sem formatação ainda)
  processed_path = save_to_excel(df, 'AL-E2-tratado')

  # Aplica a formatação visual
  format_excel(processed_path)

  print('Processo concluído com sucesso.')

if __name__ == "__main__":
  main()