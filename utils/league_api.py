import os

import requests
from dotenv import load_dotenv
load_dotenv()


def get_newest_version():
    versions = requests.get("https://ddragon.leagueoflegends.com/api/versions.json").json()
    return versions[0]


def get_game_version(version: str):
    return None


def get_key():
    api_key = os.getenv("LEAGUE_APIKEY")
    return api_key
