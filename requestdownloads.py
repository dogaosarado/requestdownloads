import os
import requests
from time import strptime

main_url = 'http://37.156.146.163/PUB/Pentester_Academy/Pentester_Academy_Web_Application_Pentesting/Pentester_Academy_Web_Application_Pentesting_ITGEEKS/'
arquivos_pasta = os.listdir('H:\projeto gustavinho proxy')
print(arquivos_pasta)
response = request.get(main_url)
colunas = response.html.find('a')
# Tupla de extensoes a serem baixadas
extensoes = ('.zip', '.mp4', '.pdf', '.html', '.php')
# Funcao para verificar se algum link possui alguma das extensoes a serem baixadas.
# Retorna True caso encontre, False no contrario 
checar_extensao = lambda link: any((ext in link for ext in extensoes))
for link in colunas:
    if checar_extensao(link.full_text):
        response = request.get(main_url + link.full_text)
        with open(link.full_text, "wb") as downloaded_file:
            downloaded_file.write(response.content)
        print('foi ok um abraço: ', link.full_text)
        print(strptime())
print(colunas)