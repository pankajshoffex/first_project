from django import forms 
from core.models import Location, Service, Login


class LocationForm(forms.ModelForm):
	class Meta:
		model = Location
		fields = ('select_loc',)
		widgets = {
			'select_loc': forms.Select(attrs={'id': 'demo'}),
		}

class ServiceForm(forms.ModelForm):
	class Meta:
		model = Service
		fields = ('select_serv',)
		widgets = {
			'select_serv': forms.Select(attrs={'id': 'demo'}),
		}

class LoginForm(forms.ModelForm):
	class Meta:
		model = Login
		confirm_password = forms.CharField(max_length=200)
		fields = '__all__'
		widgets = {
			'password':forms.PasswordInput(),
		}