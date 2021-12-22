import requests
from bs4 import BeautifulSoup as Bs

# Скрипт по сайту Нур-Султана

link = 'http://nursultan.kgd.gov.kz/ru'
# поиск ссылки Юридическим лицам
req = requests.get(link)
html = Bs(req.content, 'html.parser')
cont = html.select("#smartmenus_3 > li:nth-child(4) > a:first-child")
for a in cont:
    url = str(a.get('href'))
    break

# поиск ссылки Реабилитация и банкротсво
link1 = link + url[3:]
req1 = requests.get(link1)
html1 = Bs(req1.content, 'html.parser')
cont1 = html1.select('div.catmenu  li:nth-child(5) > a:first-child')
for a in cont1:
    url1 = str(a.get('href'))
    break

# поиск ссылок по годам 2018, 2019, 2020, 2021
link2 = link + url1[3:]
req2 = requests.get(link2)
html2 = Bs(req2.content, 'html.parser')
goda = [4, 5, 6, 8]
goda_ssylki = []  # список для ссылок по годам
for i in goda:
    cont2 = html2.select(f'div.catmenu > ul.menu > li:nth-child({i}) > a:first-child')
    for a in cont2:
        url2 = str(a.get('href'))
        goda_ssylki.append(url2)
        break

ssylki = []  # список для ссылок Информационное сообщение по годам
ssylki1 = []  # список для ссылок скачивания файлов

# поиск ссылки Информационное сообщение
for i in goda_ssylki:
    link3 = link[:-3] + str(i)
    req3 = requests.get(link3)
    html3 = Bs(req3.content, 'html.parser')
    cont3 = html3.select('div.catmenu  li:first-child > a:first-child')
    for a in cont3:
        url3 = str(a.get('href'))
        ssylki.append(url3)
        break

# поиск ссылки для скачивания файла
files = [4, 4, 4, 1]
for i in ssylki:
    link4 = link[:-3] + str(i)
    req4 = requests.get(link4)
    html4 = Bs(req4.content, 'html.parser')
    ind = ssylki.index(i)
    cont4 = html4.select(f'div.content tr:nth-child({files[ind]}) a')
    for a in cont4:
        url4 = str(a.get('href'))
        ssylki1.append(url4)
        break
# этот метод не подходит для остальных сайтов, поэтому далее ссылки введутся вручную

ssylki2 = ['']
file_num = 0
for i in ssylki1:
    resp = requests.get(i)
    output = open(f'files/{file_num}.xlsx', 'wb')
    output.write(resp.content)
    output.close()
    file_num += 1
