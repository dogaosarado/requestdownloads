import os
import requests
from requests_html import HTML, HTMLSession
from time import strptime


session = HTMLSession()

main_url = 'http://37.156.146.163/PUB/Pentester_Academy/Pentester_Academy_Web_Application_Pentesting/Pentester_Academy_Web_Application_Pentesting_ITGEEKS/'
arquivos_pasta = os.listdir('H:\projeto gustavinho proxy')
print(arquivos_pasta)
r = session.get(main_url)
colunas = r.html.find('a')
for link in colunas:
    if '.zip' in link.full_text:
        download = requests.get(main_url + link.full_text, stream=True)
        downloaded_file = open(link.full_text, "wb")
        for chunk in download.iter_content(chunk_size=2048):
            if chunk:
                downloaded_file.write(chunk)
        print('foi ok um abraço: ', strptime())
    if '.mp4' in link.full_text:
        download = requests.get(main_url + link.full_text, stream=True)
        downloaded_file = open(link.full_text, "wb")
        for chunk in download.iter_content(chunk_size=2048):
            if chunk:
                downloaded_file.write(chunk)
        print('foi ok um abraço: ', strptime())
    if '.pdf' in link.full_text:
        download = requests.get(main_url + link.full_text, stream=True)
        downloaded_file = open(link.full_text, "wb")
        for chunk in download.iter_content(chunk_size=2048):
            if chunk:
                downloaded_file.write(chunk)
        print('foi ok um abraço: ', strptime())
    if '.html' in link.full_text:
        download = requests.get(main_url + link.full_text, stream=True)
        downloaded_file = open(link.full_text, "wb")
        for chunk in download.iter_content(chunk_size=2048):
            if chunk:
                downloaded_file.write(chunk)
        print('foi ok um abraço: ', strptime())
    if '.php' in link.full_text:
        download = requests.get(main_url + link.full_text, stream=True)
        downloaded_file = open(link.full_text, "wb")
        for chunk in download.iter_content(chunk_size=2048):
            if chunk:
                downloaded_file.write(chunk)
        print('foi ok um abraço: ', link.full_text)
        print(strptime())

print(colunas)