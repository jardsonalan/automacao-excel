from data_loader import load_excel
from data_cleaner import rename_headers, correction_datas
from excel_utils import filter_datas, save_to_excel

def main():
  df = load_excel('./data/raw/AL-E2.xls')
  rename = rename_headers(df)
  correct_datas = correction_datas(rename)
  filters = filter_datas(correct_datas)
  save_to_excel('AL-E2-tratado', filters)
  print('Processo concluído com sucesso.')

if __name__ == "__main__":
  main()