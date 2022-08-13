from django.shortcuts import redirect, render
from . models import User, UserManager, Trip
from django.contrib import messages
import bcrypt
from django.db.models import Q
from .forms import TripForm
from django.core.files.storage import FileSystemStorage

# Create your views here.
def index(request):
    return render(request, 'index.html')

def signup(request):

    return render(request, 'signup.html')

def register(request):
    print(request.POST)
    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
    errors = User.objects.registrationValidator(request.POST)
    print(errors)
    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect("/")
    hashedpw = bcrypt.hashpw(request.POST['pass'].encode(), bcrypt.gensalt()).decode()
    new_user = User.objects.create(
        firstName = request.POST['fname'],
        lastName = request.POST['lname'],
        email = request.POST['email'],
        username = request.POST['uname'],
        password = hashedpw,
    )
    print(new_user)
    request.session['loggedInID'] = new_user.id
    print("$$$$$$$$$$$$$This is the user in session$$$$$$$$$$$$")
    print(request.session['loggedInID'])

    return redirect('/home')

def dashboard(request):

    trips = Trip.objects.all()
    loggedInUser = User.objects.get(id = request.session['loggedInID'])
    context = {
        'loggedInUser': loggedInUser,
        'trips': trips,
    }
    return render(request, 'home.html', context)

def login(request):
    errors = User.objects.loginValidator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request,value)
        return redirect("/")
    user = User.objects.get(email = request.POST['email'])
    request.session['loggedInID'] = user.id
    return redirect("/home")

def signIn(request):

    return render(request, 'signin_form.html')

def logout(request):
    request.session.clear()
    return redirect("/") 

def tripAdd(request):
    form = TripForm()
    if request.method == 'POST':
        form = TripForm(request.POST, request.FILES)
        if form.is_valid():
            # form.photo = form.cleaned_data["photo"]
            form.save()
        else:
            form.save()
    print(request.POST, request.FILES)
    redirect('/home')
    return render(request, 'tripAdd.html', { 'form': form})

def createTrip(request):
    trip_creator = User.objects.get(id = request.session['loggedInID'])
    newTrip = Trip.objects.create(
        city = request.POST['city'],
        country = request.POST['country'],
        description = request.POST['description'],
        creator = trip_creator,
        photo = request.FILES['photo']
    )
    print(newTrip)
    return redirect('/home')