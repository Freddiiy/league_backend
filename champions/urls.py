from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_champions),
    path('/<str:champ_name>', views.get_champ),
    path('/asset/<str:champ_name>', views.get_champ_asset)
]
