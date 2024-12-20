from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .models import Boardgame
from .forms import BoardgameForm, DescriptionForm

# Existing views
def index(request):
    return render(request, "Bp/index.html")

def boardgames(request):
    boardgames = Boardgame.objects.order_by('pub_year')
    context = {'boardgames': boardgames}
    return render(request, 'Bp/boardgames.html', context)

def boardgame(request, boardgame_id):
    boardgame = get_object_or_404(Boardgame, id=boardgame_id)
    descriptions = boardgame.descriptions.order_by('-date_added')  # Using the related_name

    context = {
        'Boardgame': boardgame,
        'descriptions': descriptions,
    }
    return render(request, 'Bp/boardgame.html', context)

def new_game(request):
    if request.method != 'POST':
        form = BoardgameForm()
    else:
        form = BoardgameForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('Bp:boardgames')

    context = {'form': form}
    return render(request, 'Bp/new_game.html', context)

def new_description(request, boardgame_id):
    boardgame = get_object_or_404(Boardgame, id=boardgame_id)

    if request.method != 'POST':
        form = DescriptionForm()
    else:
        form = DescriptionForm(data=request.POST)
        if form.is_valid():
            new_desc = form.save(commit=False)
            new_desc.title = boardgame  # Associate with the Boardgame
            new_desc.save()
            return redirect('Bp:boardgame', boardgame_id=boardgame.id)

    context = {'boardgame': boardgame, 'form': form}
    return render(request, 'Bp/new_description.html', context)

# New signup view
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully!')
            return redirect('Bp:login')  # Redirect to login page after successful signup
    else:
        form = UserCreationForm()

    return render(request, 'Bp/signup.html', {'form': form})
