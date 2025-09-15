import tkinter as tk
from tkinter import filedialog, messagebox
import os

from data_loader import load_excel
from data_cleaner import rename_headers, correction_datas
from excel_utils import filter_datas, save_to_excel
from excel_formatter import format_excel

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
    header = int(entry_header.get())
    nrows = int(entry_nrows.get())

    # Carrega a planilha
    df = load_excel(file_path, header=header, nrows=nrows)
    # Renomeia o cabeçalho
    df = rename_headers(df)
    # Corrije os dados errados
    df = correction_datas(df)
    # Filtra os dados necessários
    df = filter_datas(df)

    output_file = filedialog.asksaveasfilename(
        title="Salvar planilha tratada como...",
        defaultextension=".xlsx",
        filetypes=[("Excel files", "*.xlsx")],
        initialfile=os.path.splitext(os.path.basename(file_path))[0] + "-tratado.xlsx"
    )

    if not output_file:
      messagebox.showwarning("Aviso", "Operação cancelada pelo usuário!")
      return
    
    save_to_excel(df, output_file)
    format_excel(output_file)

    messagebox.showinfo(
      'Sucesso',
      f'Processo concluído!\n\nPlanilha salva em: \n{output_file}'
    )
  except Exception as e:
    messagebox.showerror('Erro', str(e))

def main():
  global entry, entry_header, entry_nrows

  root = tk.Tk()
  root.title('Automação Excel')
  root.geometry('500x500')

  entry = tk.Entry(root, width=60)
  entry.pack(pady=10)

  btn_select = tk.Button(root, text='Selecionar uma planilha', command=select_file)
  btn_select.pack(pady=5)

  frame_header = tk.Frame(root)
  frame_header.pack(pady=5)
  tk.Label(frame_header, text="Linha do cabeçalho:").pack(side=tk.LEFT, padx=5)
  entry_header = tk.Spinbox(frame_header, from_=0, to=100, width=5)
  entry_header.delete(0, tk.END)
  entry_header.insert(0, "17")
  entry_header.pack(side=tk.LEFT)

  frame_nrows = tk.Frame(root)
  frame_nrows.pack(pady=5)
  tk.Label(frame_nrows, text="Quantidade de dados:").pack(side=tk.LEFT, padx=5)
  entry_nrows = tk.Spinbox(frame_nrows, from_=1, to=1000, width=5)
  entry_nrows.delete(0, tk.END)
  entry_nrows.insert(0, "15")  # valor padrão
  entry_nrows.pack(side=tk.LEFT)

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