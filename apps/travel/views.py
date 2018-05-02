from django.shortcuts import render, HttpResponse, redirect
from ..login.models import User
from .models import Trip
from django.contrib import messages

# Create your views here.
# index "/"
def home(request):
    # check if what u put (email, first_name or user) in session is present
    if 'id' not in request.session: 
        return redirect('/')   
    else:
        context = {
            # needs improvement here, will revisit later
            'current_user': User.objects.get(id=request.session['id']),           
            'other_users': User.objects.all().exclude(id=request.session['id'])   
        }
    return render(request, "travel/home.html", context)

def planAdd(request):
    print "add page rendered to viewer, yeahhhhhhhhhhhhhhhhhhhh!!!!"
    return render(request, "travel/addTravel.html")

def tripAdd(request):
    current_user = User.objects.get(id=request.session["id"])
    results = Trip.objects.trip_validator(request.POST)   # Returned results from validation. 
    if results['status'] == True:
        trip = Trip.objects.trip_creator(request.POST, current_user)
        messages.success(request, "Trip successfully added!!")
        print (trip.id, "# testing here from VIEWS@@@@@@@@@")
        print (trip.description, "# testing here from VIEWS!!!!")
        print (request.session["id"], "# testing which ID here from VIEWS!!!!")
    else:
        for error in results['errors']:
            messages.error(request, error)   
            return redirect("/travels/add")         
    return redirect("/travels")

def showAttack(request):
    return render(request, "travel/attacker.html")

def showDestination(request, trip_id):
    context = {
        'trip': Trip.objects.get(id = trip_id)
    }
    print (trip_id + "  # TRIP ID testing from VIEWSshow$$$$$$$$$$$$$$$")
    return render(request, "travel/showDest.html", context)

def joinTrip(request, trip_id):
    joinedTrip = Trip.objects.get(id = trip_id)
    traveler = User.objects.get(id=request.session['id'])
    traveler.allTrips.add(joinedTrip)
    traveler.save()
    return redirect("/travels")




