from django.shortcuts import render,redirect, get_object_or_404
from .models import Boardgame
from .forms import BoardgameForm, DescriptionForm
from .models import Boardgame, Loan
from django.http import HttpResponse
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
# Create your views here.

def index(request):
    return render(request, "Bp/index.html")

def boardgames(request):
    boardgames= Boardgame.objects.all() #order_by('pub_year')
    context = {'boardgames': boardgames}
    return render(request, 'Bp/boardgames.html', context)

#def boardgame(request, boardgame_id):
    #boardgame = Boardgame.objects.get(id=boardgame_id)
    #description = Boardgame.description_set.order_by('-date_added')
    #context = {'Boardgame': boardgame, 'description': description}
    #return render(request, 'Bp/boardgame.html', context)

#def boardgame(request, boardgame_id):
    #boardgame = get_object_or_404(Boardgame, id=boardgame_id)
    #description = boardgame.description_set.all().order_by('-date_added')
    #context = {'boardgame': boardgame, 'description': description}
    #return render(request, 'Bp/boardgame.html', context)
def boardgame(request, boardgame_id):
    try:
        boardgame = Boardgame.objects.get(id=boardgame_id)
        # Use .all() to get related descriptions, but check if any exist
        descriptions = boardgame.descriptions.all().order_by('-date_added') if boardgame.descriptions.exists() else []
    except Boardgame.DoesNotExist:
        # Handle case if the boardgame does not exist
        boardgame = None
        descriptions = []
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

#def new_description(request, boardgame_id):
    #boardgame = Boardgame.objects.get(id=boardgame_id)

    #if request.method != 'POST':
      #  form = DescriptionForm()
    #else:
    #    form = DescriptionForm(data=request.POST)
    #    if form.is_valid():
    #        new_description = form.save(commit=False)
     #       new_description.boardgame = boardgame
    #        new_description.save()
    #        return redirect('Bp:boardgame', boardgame_id=boardgame_id)

   # context = {'boardgame': boardgame, 'form': form}


   # return render(request, 'Bp/new_description.html', context)

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

@login_required
def borrow_game(request, boardgame_id):
    boardgame = get_object_or_404(Boardgame, id=boardgame_id)

    # Check if the user has already borrowed 3 games
    loan_count = Loan.objects.filter(borrower=request.user, returned=False).count()
    if loan_count >= 3:
        return HttpResponse("You can only borrow up to 3 games at a time.", status=400)

    # Check if the game is available
    if not boardgame.is_available():
        return HttpResponse("Sorry, this game is currently unavailable.", status=400)

    # Create a new loan entry
    loan = Loan.objects.create(
        boardgame=boardgame,
        borrower=request.user,
        date_due=timezone.now() + timezone.timedelta(days=7),  # Set due date to 7 days from now
    )
    # Decrease the number of available copies
    boardgame.available_copies -= 1
    boardgame.save()

    return redirect('Bp:boardgame', boardgame_id=boardgame.id)

@login_required
def return_game(request, loan_id):
    loan = get_object_or_404(Loan, id=loan_id)

    # Check if the logged-in user is the borrower
    if loan.borrower != request.user:
        return HttpResponse("You are not authorized to return this game.", status=403)

    # Mark the game as returned
    loan.returned = True
    loan.save()

    # Increase the available copies of the boardgame
    loan.boardgame.available_copies += 1
    loan.boardgame.save()

    return redirect('Bp:boardgame', boardgame_id=loan.boardgame.id)

@login_required
def overdue_loans(request):
    overdue_loans = Loan.objects.filter(borrower=request.user, returned=False, date_due__lt=timezone.now())

    context = {
        'overdue_loans': overdue_loans
    }
    return render(request, 'Bp/overdue_loans.html', context)





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