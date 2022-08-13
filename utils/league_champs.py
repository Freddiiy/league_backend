import requests

import utils.league_api


def get_champions():
    newest_version = utils.league_api.get_newest_version()
    return get_champions_version(newest_version)


def get_champions_version(version: str):
    return requests.get(f"https://ddragon.leagueoflegends.com/cdn/{version}/data/en_US/champion.json").json()


def get_champ(champ: str):
    champ = champ.capitalize()
    return requests.get(f"https://ddragon.leagueoflegends.com/cdn/12.15.1/data/en_US/champion/{champ}.json").json()


def get_champ_img(champ: str):
    champ = champ.capitalize()
    champ_assets = {
        "spash": f"https://ddragon.leagueoflegends.com/cdn/img/champion/splash/{champ}_0.jpg",
        "loading": f"https://ddragon.leagueoflegends.com/cdn/img/champion/loading/{champ}.jpg",
        "square": f"https://ddragon.leagueoflegends.com/cdn/img/champion/loading/{champ}_0.jpg",
    }
    return champ_assets
