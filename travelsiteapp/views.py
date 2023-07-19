from multiprocessing import context
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

    return render(request, 'signup2.html')

def register(request):
    print(request.POST)
    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
    errors = User.objects.registrationValidator(request.POST)
    print(errors)
    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect("/signup")
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
    
    if(request.session):
        loggedInUser = User.objects.get(id = request.session['loggedInID'])
        context = {
            'loggedInUser': loggedInUser,
            'trips': trips,
        }
        print('**************made it here*****************')
        return render(request, 'home.html', context)
    else:
        return redirect('/')
        

    

def login(request):
    errors = User.objects.loginValidator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request,value)
        return redirect("/signin")
    user = User.objects.get(email = request.POST['email'])
    request.session['loggedInID'] = user.id
    return redirect("/home")

def signIn(request):

    return render(request, 'signin2.html')

def logout(request):
    request.session.clear()
    print("******************You logged out****************")
    return redirect("/") 

def tripAdd(request):
    form = TripForm()
    if request.method == 'POST':
        form = TripForm(request.POST, request.FILES)
        if form.is_valid():
            # form.photo = form.cleaned_data["photo"]
            form.save()
        else:
            return redirect('/new_trip')
    print(request.POST, request.FILES)
    redirect('/home')
    return render(request, 'tripAdd2.html', { 'form': form})

def createTrip(request):
    trip_creator = User.objects.get(id = request.session['loggedInID'])
    all_trips = Trip.objects.all()
    newTrip = Trip.objects.create(
        city = request.POST['city'],
        country = request.POST['country'],
        continent = request.POST['continent'],
        description = request.POST['description'],
        creator = trip_creator,
        photo_url = request.POST['photo_url']
    )
    print(newTrip)
    print(all_trips)
    return redirect('/home')

def continentsPage(request):
    print("**********************get example_trip***************")
    # example_trip = Trip.objects.get(id = request.session['trip_continent_id'])
    trips = Trip.objects.filter(continent = request.session['continent'])
    context ={
        'trips': trips,
    }
    del request.session['continent']
    request.session.modified = True
    return render(request, "continents2.html", context)
    

def showTripByContinent(request):
    print("**********************get trip_continent***************")
    print("This is req.POST[continent]: " , request.POST['continent'])
    continent = request.POST['continent']
    request.session['continent'] = continent
    print(request.session['continent'])
    # trip_continent = Trip.objects.filter(continent = request.POST['continent'])[:1].get()
    # print("********************************************************")
    # print(trip_continent)
    # request.session['trip_continent_id'] = trip_continent.id
    # print("********************************************************")
    # print(request.session['trip_continent_id'])
    # print("********************************************************")
    return redirect('/continents')