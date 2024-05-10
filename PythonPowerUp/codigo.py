# Passo a passo do projeto

#sempre utilizar o comando: python -m venv venv | para usar o codigo em um "ambiente virtual"

# 1. Abrir o sistema da empresa 
    # https://dlp.hashtagtreinamentos.com/python/intensivao/login

# para instalar: pip install pyautogui
import pyautogui
import time

pyautogui.PAUSE = 0.5

# pyautogui.click -> clicar com o mouse rafael.b.villela@gmail.com
# pyautogui.write -> escrever um texto
# pyautogui.press -> pressionar uma tecla do teclado
# pyautogui.hotckey -> apertar um conjunto de teclas (Ctrl C, Ctrl V, Alt Tab)

# abrir o navegador 
pyautogui.press("win")
pyautogui.write("opera")
pyautogui.press("enter")

# entrar no site do sistema
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

# aqui pode ser que ele demore alguns segundos para carregar o site
time.sleep(2)

# 2. Fazer login
pyautogui.click(x=863, y=391) # depois das cordenadas da para colocar uma virgula e escrever button e o botao que vc quer ou digitar click 2 para dar double click

pyautogui.write("rafael.b.villela@gmail.com")
pyautogui.press("tab")
pyautogui.write("minha senha")

pyautogui.press("tab")
pyautogui.press("enter")

time.sleep(2)

# 3. Abrir/Importar a base de dados de produtos para cadastrar 
# pip install pandas, numpy e openpyxl
import pandas as pd # para poder mudar o nome da variavel pode colocar as e o nome que voce quer 

tabela = pd.read_csv("D:\FIAP\Python\PythonPowerUp\produtos.csv")

print(tabela)

# 4. Cadastrar um produto

for linha in tabela.index:
    # clicar no campo de código
    pyautogui.click(x=766, y=270)

    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(codigo)
    # pegar da tabela o valor do campo que a gente quer preencher
    # passar para o proximo campo
    pyautogui.press("tab")
    # preencher o campo
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
    obs = tabela.loc[linha, "obs"]
    if not pd.isna(obs): # ou if obs != "nan"
        pyautogui.write(str(tabela.loc[linha, "obs"]))
    pyautogui.press("tab")
    pyautogui.press("enter") # cadastra o produto (botao enviar)
    # dar scroll de tudo pra cima
    pyautogui.scroll(5000)

# 5. Repetir isso tudo até acabar a lista de produtos