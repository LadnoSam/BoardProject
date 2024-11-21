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
    #path('boardgames/<int:boardgame_id>/', views.boardgame, name='boardgame'),
    path('boardgames/new_description/<int:boardgame_id>/', views.new_description, name='new_description'),

    path('boardgames/<int:boardgame_id>/', views.boardgame, name='boardgame'),
    path('boardgames/borrow/<int:boardgame_id>/', views.borrow_game, name='borrow_game'),
    path('boardgames/return/<int:loan_id>/', views.return_game, name='return_game'),
    path('overdue_loans/', views.overdue_loans, name='overdue_loans'),




]