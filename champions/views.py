import requests
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

from utils import league_champs


@api_view(['GET'])
def get_champions(request):
    return Response(league_champs.get_champions())


@api_view(['GET'])
def get_champ(request, champ_name: str):
    return Response(league_champs.get_champ(champ_name))


@api_view(['GET'])
def get_champ_asset(request, champ_name: str):
    return Response()
