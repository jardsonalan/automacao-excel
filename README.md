# Automação Excel

![GitHub pull requests](https://img.shields.io/github/issues-pr/jardsonalan/automacao-excel)
![GitHub issues](https://img.shields.io/github/issues/jardsonalan/automacao-excel)
![GitHub stars](https://img.shields.io/github/stars/jardsonalan/automacao-excel)
![GitHub forks](https://img.shields.io/github/forks/jardsonalan/automacao-excel)

Automação feita em Python utilizando pandas, tkinter, openpyxl e xlrd para facilitar na formatação de planilhas Excel.

## Sumário
- [Tecnologias Utilizadas](#tecnologias-utilizadas)
- [Arquitetura](#arquitetura)
- [Pré-requisitos](#pré-requisitos)
- [Instalação](#instalação)
- [Execução](#execução)
- [Contribuindo](#contribuindo)

## Tecnologias Utilizadas
- **Linguagens:** Python
- **Bibliotecas:** pandas, openpyxl, tkinter, xlrd

## Arquitetura
```bash
automacao-excel/
│
├── data/                          # Dados utilizados no projeto
│   ├── raw/                       # Planilhas brutas (entrada)
│   ├── processed/                 # Dados intermediários ou limpos
│   └── output/                    # Resultados finais gerados pelo script
│
├── src/                           # Código-fonte principal
│   ├── __init__.py                # Torna o diretório um pacote Python
│   ├── main.py                    # Script principal que executa a automação
│
│   ├── data_loader.py             # Funções para carregar arquivos Excel
│   ├── data_cleaner.py            # Limpeza e pré-processamento dos dados
│   ├── excel_formatter.py         # Estilização e formatação das planilhas
│   └── excel_utils.py             # Funções auxiliares para manipulação de Excel
│
├── .gitignore                     # Arquivos/pastas a serem ignorados pelo Git
├── LICENSE                        # Licença do projeto (ex: MIT)
├── README.md                      # Documentação principal do projeto
└── requirements.txt               # Lista de dependências do Python
```

## Pré-requisitos
Certifique-se que você tem instalado:
- [Python](https://www.python.org/downloads/)

## Instalação
```bash
# Clone o repositório
git clone https://github.com/jardsonalan/automacao-excel.git

# Entre no diretório
cd automacao-excel

# Instale as bibliotecas
pip install -r requirements.txt
```

## Execução
### Distribuições Linux
- Crie uma máquina virtual (`venv`) para rodar o projeto:

  ```bash
  # Comando para criar a máquina virtual 
  python3 -m venv nome-da-maquina

  # Comando para inicializar a máquina virtual
  source nome-da-maquina/bin/activate

  # Comando para desativar a máquina virtual
  deactivate
  ```
- Certifique-se que tem o Tkinter instalado:

  ```bash
  python3 -m tkinter
  ```

- Comandos de instalação do Tkinter:

  ```bash
  # Ubuntu / Debian / Linux Mint:
  sudo apt update
  sudo apt install python3-tk
  
  # Fedora:
  sudo dnf install python3-tkinter
  
  # Arch Linux / Manjaro:
  sudo pacman -S tk
  ```

## Contribuindo
1. Faça um fork do projeto;
2. Crie uma branch (`git checkout -b minha-feature`);
3. Commit suas mudanças (`git commit -m 'Adiciona minha feature'`);
4. Envie para o repositório (`git push origin minha-feature`);
5. Abra um Pull Request.
