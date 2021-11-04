from pprint import pprint

import requests

access_token = 2619421814940190


class SuperHero:
    def __init__(self, access_token, hero_name):
        self.token = access_token
        self.hero_name = hero_name
        self.hero_intelligence = None

    def get_hero_intelligence(self):
        hero_url = 'https://superheroapi.com/api/{}/search/{}'.format(self.token, self.hero_name)
        response = requests.get(hero_url)
        for hero in response.json()['results']:
            if hero['name'] == self.hero_name:
                self.hero_intelligence = int(hero['powerstats']['intelligence'])


Hulk = SuperHero(access_token, 'Hulk')
Hulk.get_hero_intelligence()

Captain_America = SuperHero(access_token, 'Captain America')
Captain_America.get_hero_intelligence()

Thanos = SuperHero(access_token, 'Thanos')
Thanos.get_hero_intelligence()

super_heroes = [Hulk, Captain_America, Thanos]


def func(super_hero):
    return super_hero.hero_intelligence


print(max(super_heroes, key=func).hero_name)
