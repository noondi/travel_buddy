from django.shortcuts import render, HttpResponse, redirect
from models import User
from django.contrib import messages

# Create your views here.
# index "/"
def index(request):
    # User.objects.all().delete()
    return render(request, "login/index.html")

def register(request):
    results = User.objects.validate(request.POST)   # Returned results from validation.  
    if results['status'] == True:
        user = User.objects.creator(request.POST)
        messages.success(request, "User successfully createdd!!!")  
    else:
        for error in results['errors']:
            messages.error(request, error) 
    return redirect("/")

def login(request):
    results = User.objects.loginValidator(request.POST)
    if results['status'] == False:
        messages.error(request, 'Please check your email or password and try again!!')
        return redirect('/')
    # otherwise login in the user and put him in session
    request.session['email'] = results['user'].email
    request.session['first_name'] = results['user'].first_name
    request.session['id'] = results['user'].id  
    
    print request.session['first_name']  
    print request.session["id"]
    print request.session["email"]
 
    return redirect('/travels')

def logout(request):    
    # request.session.flush()
    request.session.clear()
    return redirect('/')