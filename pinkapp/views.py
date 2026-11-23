from django.shortcuts import render, redirect, get_object_or_404
from pinkapp.models import *



#Authentication Imports
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

# Create your views here.
def error(request):
    return render(request, '404.html')

def details(request):
    return render(request, 'blog-details.html')

def blog(request):
    return render(request, 'blog.html')

def index(request):

    if request.method == 'POST': 
        mycontact = Contact(
             name = request.POST['name'],
             email = request.POST['email'],
             subject = request.POST['subject'],
             message = request.POST['message'],




        )
        mycontact.save()
        return redirect('/')
    else:
        return render(request, 'index.html')

    

def portfolio(request):
    return render(request, 'portfolio-details.html')

def service(request):
    return render(request, 'service-details.html')

def starter(request):
    return render(request, 'starter-page.html')

def show(request):
    all = Contact.objects.all()
    return render(request, 'show.html', { "all": all})


def delete(request, id):
    contactinfo = Contact.objects.get(id=id)
    contactinfo.delete()
    return redirect('/show')


def edit(request, id):
    editcontact = get_object_or_404(Contact, id=id)

    if request.method == "POST":
        editcontact.name = request.POST.get('name')
        editcontact.email = request.POST.get('email')
        editcontact.subject = request.POST.get('subject')
        editcontact.message = request.POST.get('message')

        editcontact.save()
        return redirect('/show')
    else:
        return render(request, 'edit.html')

        

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.db import IntegrityError

def register(request):
    """Show the registration form"""

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        # Check whether passwords match
        if password == confirm_password:
            try:
                user = User.objects.create_user(
                    username=username,
                    password=password
                )

                messages.success(request, "Account created successfully")
                return redirect('/login')

            except IntegrityError:
                messages.error(request, "Username already exists")

        else:
            messages.error(request, "Passwords do not match")

    return render(request, 'register.html')



def login_view(request):
    return render(request, 'login.html') 
     if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        # Check if the user exists
        if user is not None:
            # login(request, user)
            login(request,user)
            messages.success(request, "You are now logged in!")
            # Admin
            if user.is_superuser:
                return redirect('/show')

            # For Normal Users
            return redirect('/index')
        else:
            messages.error(request, "Invalid login credentials")

    return render(request, 'login.html')


            