import requests
from pprint import pprint

TOKEN = "2619421814940190"

urls = []
uper = []


def napolnenie():
    super = input('Введите имя супергероя для сравнения: ')
    uper.append(super)
    urll = f'https://www.superheroapi.com/api.php/{TOKEN}/search/'
    urls.append(urll + super.replace(' ', '%'))
    print(uper)
    return urls


while True:
    napolnenie()
    comand = input('Для добавления следущего героя нажмите Enter, \nесли хотите сравнить введите s : ')
    if comand == 's':
        break


def requests_get(url_all):
    r = (requests.get(url) for url in url_all)
    return r


super_man = []


def parser():
    for item in requests_get(urls):
        intelligence = item.json()
        for power_stats in intelligence['results']:
            super_man.append({
                'name': power_stats['name'],
                'intelligence': power_stats['powerstats']['intelligence'],
            })
            # for data in super_man:
    #   if data.get('intelligence') == 'null':
    #     super_man.remove(data)
    #     print('\nЗначения null удалены\n')
    pprint(super_man)

    for data in super_man:

        if data.get('intelligence') == 'null':
            super_man.remove(data)
    print('\nЗначения null удалены\n')
    maxintelligence = max(super_man, key=lambda x: x['intelligence'])
    pprint(maxintelligence)
    # Сравним интеллекты героев
    pprint(super_man)

    intelligence_hero = 0
    for intel_hero in super_man:
        if intelligence_hero < int(intel_hero['intelligence']):
            intelligence_hero = int(intel_hero['intelligence'])
            name = intel_hero['name']

    print(f"\nСамый интеллектуальный {name}, интеллект: {intelligence_hero} {maxintelligence} ")


parser()
