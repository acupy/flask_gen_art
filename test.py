import requests
import shutil

url = 'https://www.floydlabs.com/expose/PLpMoND7crRQcFD2fPpLUc'
files = { 'file':open('./images/66/taipei101.jpg') }
path = './output.jpg'
r = requests.post(url, files=files, stream=True)

if r.status_code == 200:
    with open(path, 'wb') as f:
        r.raw.decode_content = True
        shutil.copyfileobj(r.raw, f)
