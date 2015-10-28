from django.shortcuts import render
from core.models import Location, Service, Login, CustomerEnquiry
from core.forms import LocationForm, ServiceForm, LoginForm
from django.http import HttpResponse
# Create your views here.
def index(request):
	 
	if request.method == 'POST':
		form = LocationForm(request.POST)
		if form.is_valid():
			ax = form.cleaned_data['select_loc']
			print ax	
	else:
		form = LocationForm()


	if request.method == 'POST':
		form1 = ServiceForm(request.POST)
		if form1.is_valid():
			ser = form1.cleaned_data['select_serv']
			print ser	
	else:
		form1 = ServiceForm()
	
	return render(request, 'core/index.html', {'form':form, 'form1':form1})

def sign_up(request):
	if request.method == 'POST':
		
		form = LoginForm(request.POST)
		if form.is_valid():
			first_pass = form.cleaned_data['password']
			conf_pass = request.POST.get("confpass", "")
			
			if not conf_pass:
				return HttpResponse("Please Enter Confirm password")
				
			if first_pass != conf_pass:
				return HttpResponse("Your passwords do not match")
			else:
				print first_pass
				print conf_pass
				form.save()
	else:
		form = LoginForm()

	return render(request, 'core/login.html', {'form':form})


def demo(request):
	if request.method == 'POST':
		location = request.POST["loc"]
		print location
		# serv1 = request.POST.get("serv")
		# obj = CustomerEnquiry.objects.create(city=location, service=serv1)
		# print obj.city
	return render(request, 'index.html', {})


