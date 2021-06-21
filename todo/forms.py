from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from ckeditor.widgets import CKEditorWidget
from .models import *

			
class ProfileForm(UserCreationForm):
	class Meta:
		model = Profile
		fields = ['username', 'password1', 'password2', 'email', 'first_name', 'last_name', 'gender', 'phone_number','age']
     
class InterestForm(ModelForm):
	interests = forms.CharField(max_length=50)
	class Meta:
		model = Interests
		fields = ['interests']
 
     
class CreateNoteForm(ModelForm):
	content = forms.CharField(widget=CKEditorWidget())
	
	class Meta:
		model = Note
		fields = '__all__'
		
class CreateChaklengeForm(ModelForm):
    class Meta:
        model = Challenge
        fields = '__all__'