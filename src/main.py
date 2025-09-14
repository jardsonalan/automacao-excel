import tkinter as tk
from tkinter import filedialog, messagebox
import os

from data_loader import load_excel
from data_cleaner import rename_headers, correction_datas
from excel_utils import filter_datas, save_to_excel
from excel_formatter import format_excel

OUTPUT_DIR = './data/processed'

def select_file():
  file_path = filedialog.askopenfilename(
    title='Selecione uma planilha Excel',
    filetypes=[('Planilhas Excel', '*.xls *.xlsx')]
  )
  if file_path:
    entry.delete(0, tk.END)
    entry.insert(0, file_path)

def run_process():
  file_path = entry.get()

  if not file_path or not os.path.exists(file_path):
    messagebox.showwarning('Aviso', 'Selecione um arquivo válido!')
    return
  
  try:
    # Carrega a planilha
    df = load_excel(file_path)
    # Renomeia o cabeçalho
    df = rename_headers(df)
    # Corrije os dados errados
    df = correction_datas(df)
    # Filtra os dados necessários
    df = filter_datas(df)

    os.makedirs(OUTPUT_DIR, exist_ok=True)
    file_name = os.path.splitext(os.path.basename(file_path))[0]
    output_file = os.path.join(OUTPUT_DIR, f'{file_name}-tratado.xlsx')
    save_to_excel(df, output_file)

    format_excel(output_file)

    messagebox.showinfo(
      'Sucesso',
      f'Processo concluído!\n\nPlanilha salva em: \n{output_file}'
    )
  except Exception as e:
    messagebox.showerror('Erro', str(e))

def main():
  global entry

  root = tk.Tk()
  root.title('Automação Excel')
  root.geometry('500x500')

  entry = tk.Entry(root, width=60)
  entry.pack(pady=10)

  btn_select = tk.Button(root, text='Selecionar uma planilha', command=select_file)
  btn_select.pack(pady=5)

  btn_run = tk.Button(
    root,
    text='Rodar Automação',
    command=run_process,
    bg='green',
    fg='white',
    font=('Arial', 12, 'bold')
  )
  btn_run.pack(pady=20)

  root.mainloop()

if __name__ == "__main__":
  main()