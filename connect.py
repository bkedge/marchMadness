import requests

def make_connection(url):
    print('Connecting')
    r = requests.get(url)

    if r.status_code == 200:
        return requests.get(url)
    else:
        raise ConnectionError


url = 'https://google.com'

r = make_connection(url)
print(r)