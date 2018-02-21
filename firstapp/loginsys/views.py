# -*- coding: utf-8 -*-
from __builtin__ import str
from django.shortcuts import render_to_response, redirect
from django.contrib import auth
from django.contrib.auth import authenticate, login
from django.template.context_processors import csrf, request
from django.contrib.auth.forms import UserCreationForm

'''if request.session.test_cookie_worked():
    print ">>>> TEST COOKIE WORKED!"
    request.session.delete_test_cookie()'''

# Create your views here.
def login_user(request):
    args = {}
    args.update(csrf(request))
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            args['login_error'] = "Пользователь "+ str(username) + " не найден"
            return render_to_response('login.html', args)
    else:
        return render_to_response('login.html', args)

def logout_user(request):
    auth.logout(request)
    return redirect("/")


def register(request):
    args = {}
    args.update(csrf(request))
    args['form'] = UserCreationForm()
    if request.POST:
        newuser_form = UserCreationForm(request.POST)
        if newuser_form.is_valid():
            newuser_form.save()
            newuser = auth.authenticate(username=newuser_form.cleaned_data['username'], password=newuser_form.cleaned_data['password2'])
            auth.login(request, newuser)
            return redirect('/')
        else:
            args['form']=newuser_form
    return render_to_response('register.html', args)
