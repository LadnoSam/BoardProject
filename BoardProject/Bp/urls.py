from django.urls import path
from . import views

app_name = "Bp"

urlpatterns = [
    #home page
    path('', views.index, name='index'),

    #page for board games
    path('boardgames/', views.boardgames, name='boardgames'),
    #path('boardgames/<int:boardgame_id>/', views.boardgame, name='boardgame'),
    path('boardgames/new_game/', views.new_game, name='new_game'),
    #path('boardgames/new_description/<int:boardgame_id>/', views.new_description, name= 'new_description'),
    path('boardgames/<int:boardgame_id>/', views.boardgame, name='boardgame'),
    path('boardgames/new_description/<int:boardgame_id>/', views.new_description, name='new_description'),
]