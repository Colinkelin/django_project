#from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms  import AuthenticationForm, UserCreationForm
#The form is a class that accepts username and login credentials for a user.
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required #corresponds with the logout_view to ensure logged in user can log out.
from django.contrib import messages   
from django.views import View

def login_view(request):
    #return HttpResponse("Login view")
    if request.method == 'POST':
        login_form = AuthenticationForm(request=request, data=request.POST)
        #injecting data into the form that we got from the POST request.
        #so that now the form will have information within it that is received from the user
        if login_form.is_valid():
            username = login_form.cleaned_data.get('username')
            password = login_form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            print(user)
            if user is not None:
                login(request, user)
                messages.success(request, f'Hi {username}! You are successfully logged in')
                return redirect('home')
            else:
                messages.error(request, f'An error occured')

        else:
            messages.error(request, f'An error occured')
           
    elif request.method =='GET':
        login_form = AuthenticationForm()
    return render(request,'login.html', {'login_form': login_form})
#reference the key within the login template to get to work with the form


#def reg_view(request):
    #reg_form = UserCreationForm()
    #return render(request, 'register.html', {'reg_form':reg_form})

class reg_view(View):
    def get(self, request):   
        reg_form = UserCreationForm # code for creation of an empty registration form
        return render(request, 'register.html', {'reg_form': reg_form })

    def post(self, request):
        reg_form = UserCreationForm(data=request.POST)
        if reg_form.is_valid():
            user = reg_form.save() #saved the user object into the database after registration
            user.refresh_from_db()
            username = reg_form.cleaned_data.get('username')
            password = reg_form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, f'{username} registered successfully')
            return redirect('home')
        else:
            messages.error(request, f'An error occured')
            return render(request, 'register.html', {'reg_form':reg_form})

@login_required
def logout_view(request):
    logout(request)
    return redirect('main')


# Create your views here.