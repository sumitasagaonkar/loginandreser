from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
from .forms import CreateUserForm

from django.contrib.auth import authenticate , login,logout
from django.contrib import messages

def index(request):
	context = {}
	return render(request, 'home.html',context)

def registerPage(request):
	form = CreateUserForm()

	if request.method == "POST":
		form = CreateUserForm(request.POST)
		if form.is_valid():  
			form.save()
			user = form.cleaned_data.get('username')
			messages.success(request, 'Account was created for  '+ user)
			return redirect('login');


	context = {'form': form}
	return render(request, 'register.html',context)

def loginPage(request):

	if request.method == "POST":
		username= request.POST.get("username")
		password = request.POST.get("password")

		user = authenticate(request, username =username , password = password)

		if user is not None:
			login(request, user)
			return redirect('index')
		else:
			messages.info(request,"username pass incorext")



	context = {}
	return render(request,'login.html', context)



def logoutUser(request):
	logout(request)

	return redirect('login')