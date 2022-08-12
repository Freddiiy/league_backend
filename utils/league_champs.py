import requests

import utils.league_api


def get_champions():
    newest_version = utils.league_api.get_newest_version()
    return get_champions_version(newest_version)


def get_champions_version(version: str):
    return requests.get(f"https://ddragon.leagueoflegends.com/cdn/{version}/data/en_US/champion.json").json()


def get_champ(champ_name: str):
    champ_name = champ_name.capitalize()
    return requests.get(f"https://ddragon.leagueoflegends.com/cdn/12.15.1/data/en_US/champion/{champ_name}.json").json()


def get_champ_img(champ_name: str):
    return requests.get(f"https://ddragon.leagueoflegends.com/cdn/12.15.1/img/champion/{champ_name}.png").json()
