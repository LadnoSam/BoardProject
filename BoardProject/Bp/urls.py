from django.urls import path
from django.contrib.auth import views as auth_views  # Import auth_views here
from . import views

app_name = "Bp"

urlpatterns = [
    # Home page
    path('', views.index, name='index'),

    # Page for board games
    path('boardgames/', views.boardgames, name='boardgames'),
    # path('boardgames/<int:boardgame_id>/', views.boardgame, name='boardgame'),
    path('boardgames/new_game/', views.new_game, name='new_game'),
    # path('boardgames/new_description/<int:boardgame_id>/', views.new_description, name= 'new_description'),
    path('boardgames/<int:boardgame_id>/', views.boardgame, name='boardgame'),
    path('boardgames/new_description/<int:boardgame_id>/', views.new_description, name='new_description'),

    # Authentication views
     path('login/', auth_views.LoginView.as_view(template_name='Bp/login.html'), name='login'),
     path('signup/', views.signup, name='signup'),  
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),  # Add this line
]

