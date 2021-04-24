import time

import requests


def local_server(login, password):  # Запросы на незащищенный локальный сервер
    data = {'login': login, 'password': password}
    response = requests.post('http://127.0.0.1:5000/auth', json=data)
    return response.status_code == 200


def local_server_protected(login, password, attempts=10, timeout=2):  # Запросы на защищенный локальный сервер
    data = {'login': login, 'password': password}
    for i in range(attempts):
        try:
            response = requests.post('http://127.0.0.1:4000/auth', json=data)
            if response.status_code == 200:
                return True
            elif response.status_code == 401:
                return False
        except:
            # Connection Error
            pass

        if i < attempts - 1:
            time.sleep(timeout)

    print('Не удалось проверить пару', data)
    return False


def example_com(login, password):  # Запросы на сайт
    data = {'email': login, 'password': password}
    response = requests.post('https://example.com/auth/login', data=data)
    return 'Неправильные данные для входа' not in response.text
