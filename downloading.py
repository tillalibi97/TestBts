import requests
from script import ssylki1
from manual import ssylki2

ssylki = []
ssylki.extend(ssylki1)
ssylki.extend(ssylki2)
file_num = 0
for i in ssylki:
    resp = requests.get(i)
    if i.endswith('x'):
        file_ext = 'xlsx'
    else:
        file_ext = 'xls'
    output = open(f'files/{file_num}.{file_ext}', 'wb')
    output.write(resp.content)
    output.close()
    file_num += 1


