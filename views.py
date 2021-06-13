from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
#from django.contrib.auth.models import Group
from .models import*
from .forms import BuyForm , CreateUserForm
from .filters import BuyFilter
from .decorators import unauthenticated_user,allowed_users,admin_only


def logoutUser(request):
	logout(request)
	return redirect('login')
	
@login_required(login_url='login')
@admin_only
def home(request):

	users = User.objects.all()
	stocks = Stock.objects.all()
	context ={'users' : users , 'stocks' : stocks}

	return render(request,'coin/dashboard.html',context)

def aboutUs(request):
	return render(request,'coin/aboutUs.html')

def services(request):
	return render(request,'coin/services.html')

def happyhour(request):
	return render(request,'coin/happyhour.html')

def buystocks(request):
	return render(request,'coin/buystocks.html')

def signin(request):
	return render(request,'coin/signin.html')

def signup(request):
	return render(request,'coin/signup.html')

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def user(request, pk_test):

	user = User.objects.get(id=pk_test)

	buys = user.buy_set.all()
	buy_count = buys.count()

	forums=user.forum_set.all()
	forum_count=forums.count()

	myFilter = BuyFilter(request.GET, queryset=buys)
	buys = myFilter.qs

	context = {'user': user,'buys': buys,'buy_count' : buy_count,'myFilter': myFilter}

	return render(request,'coin/user.html',context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])	
def stock(request , pk):
	
	buystock = Stock.objects.get(id = pk)
	stock = Stock.objects.all()

	stocks = buystock.buy_set.all()
	stock_count = stocks.count()

	
	context = {'stock':stock,'buystock' : buystock , 'stocks' : stocks ,'stock_count' : stock_count}
	return render(request,'coin/stock.html',context)




@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def buyingStock(request):

	form = BuyForm()
	if request.method == 'POST':
		#print('Printing POST:' , request.POST)
		form = BuyForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/')	



	context={'form' : form}

	return render(request , 'coin/buy_form.html' , context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def updateBuy(request,pk):

	buy = Buy.objects.get(id=pk)
	form = BuyForm(instance = buy)

	if request.method == 'POST':
		#print('Printing POST:' , request.POST)
		form = BuyForm(request.POST, instance = buy)
		if form.is_valid():
			form.save()
			return redirect('/')


	context = {'form' : form}

	return render(request , 'coin/buy_form.html' , context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def deleteBuy(request,pk):
	buy = Buy.objects.get(id=pk)
	if request.method == "POST":
		buy.delete()
		return redirect('/')
	context={'item': buy}


	return render(request,'coin/delete.html',context)


@unauthenticated_user
def registerPage(request):
	
	form = CreateUserForm()

	if request.method =="POST":
		form = CreateUserForm(request.POST)
		if form.is_valid():
			form.save()
			user = form.cleaned_data.get('user')

			#group = Group.objects.get(name='user')
			#user.groups.add(group)

			messages.success(request,'Account was created for ' + user)
			return redirect('login')




	context={'form':form}
	return render(request,'coin/register.html',context)


@unauthenticated_user
def loginPage(request):
	if request.method =="POST":
		username=request.POST.get('username')
		password=request.POST.get('password')
		user = authenticate(request,username=username,password=password)

		if user is not None:
			login(request,user)
			return redirect('home')
		else : 
			messages.info(request,'Username or password is incorrect')
					
	context={}
	return render(request,'coin/login.html',context)
	

		



def forum(request,pk):
	forum = Forum.objects.get(id=pk)

	context={}
	return render(request,'coin/forum.html',context)