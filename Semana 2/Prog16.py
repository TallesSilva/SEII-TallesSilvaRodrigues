#try and except
import requests

try:
    a = requests.get('http://www.google.com')
    print('acertou')
except Exception:
    print('errou')
