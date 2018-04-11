from django.shortcuts import render, redirect
from accounts.forms import RegistrationsForm, EditProfileForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash

# Create your views here.

def home(request):
    numbers = [1,2,3,4,5]
    name = 'Ramon Morban'
    args = {'myName':name, 'numbes':numbers}
    return render(request, 'accounts/home.html',args)


def register(request):
    if request.method =='POST':
        form = RegistrationsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/accounts')
    else:
        form = RegistrationsForm()

        args = {'form': form}
        return render(request, 'accounts/reg_form.html',args)    


def profile(request):
    args = {'user': request.user}
    return render(request, 'accounts/profile.html',args)    

def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance = request.user)
        
        if form.is_valid():
            form.save()
            return redirect('/accounts/profile')
    else:
        form = EditProfileForm(instance = request.user)
        args = {'form':form}
        return render(request, 'accounts/edit_profile.html',args) 



def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data = request.POST, user = request.user)
        
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('/accounts/profile')
        else:
            return redirect('/accounts/change_password')
    else:
        form = PasswordChangeForm(user = request.user)
        args = {'form':form}
        return render(request, 'accounts/change_password.html',args) 
    