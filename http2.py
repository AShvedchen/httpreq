import requests
from pprint import pprint

TOKEN = "2619421814940190"

urls = []

def napolnenie():
  super = list(range(1, 731 + 1))
  for numer in super:
    id = str(numer)
    urll = f'https://www.superheroapi.com/api.php/{TOKEN}/'
    urls.append(urll + id)
  return urls

napolnenie()

def requests_get(url_all):
  r = (requests.get(url) for url in url_all)
  return r

super_man = []

def parser():
  for item in requests_get(urls):
    intelligence = item.json()
    super_man.append({
      'name': intelligence['name'],
      'intelligence': intelligence['powerstats']['intelligence']
    })

parser()

def parser2():
  for data in super_man:
    if data.get('intelligence') == '100':
      pprint(f'Супергерой: {data["name"]} интелект: {data["intelligence"]}')

parser2()
