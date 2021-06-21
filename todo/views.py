from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.db.models import Q
from .models import *
from .forms import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views import View
from django.views.generic.list import ListView
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from todo.servieces import *


def register(request):
	form = ProfileForm()
	form1 = InterestForm()
	if request.method == 'POST':
		form = ProfileForm(request.POST)
		form1 = InterestForm(request.POST)
		if form.is_valid() and form1.is_valid():
			profile = form.save()
			iterests =form1.save()
			return redirect ('login')
	else:
		form = ProfileForm()
		form1 = InterestForm()
	context = {
		'form':form,
		'form1':form1
	}
	return render(request, 'registration.html', context)
	
def login_user(request):
	if request.method == "POST":
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			return redirect('/')
		else:
			return redirect('login')
		
	return render (request, 'login.html')
	
def logout_user(request):
    logout(request)
    return redirect('login')
		

class NotesList(LoginRequiredMixin, View):
	login_url = 'login/'
	def get (self, request):
		notes = Note.objects.all().order_by('-time_add')
		percents = count_percentage_completed_tasks()
		context = {
			'percents':percents,
			'notes':notes
		}
		return render(request, 'notes.html', context)
	

class CreateNote(LoginRequiredMixin, CreateView):
	#todo отображение туду листа индивидуально свои для каждого пользователя
	model = Note
	login_url = 'login/'
	template_name = 'create_note.html'
	form_class = CreateNoteForm
	success_url = '/'
	
	
	
@login_required(login_url='login/')
def NoteUpdate(request, id):
# изменение выбранной заметки
	update = Note.objects.get(id=id)
	form = CreateNoteForm(instance=update)
	if request.method == 'POST':
		form = CreateNoteForm(request.POST, instance=update)
		if form.is_valid():
			form.save()
			return redirect('/')
	return render(request,'edit.html', {'form':form})
			
			
class NoteDelete(LoginRequiredMixin, DeleteView):
#удаление выбранной заметки
	login_url = 'login/'
	model = Note
	template_name = 'delete.html'
	success_url = '/'


class BlogView(LoginRequiredMixin, ListView):
	model = Post
	login_url = 'login/'
	template_name = 'blog/blog.html'
	context_object_name = 'posts'
	ordering = '-time_add'
	
	def get_queryset(self):
		return Post.objects.all()


class ProfileView(LoginRequiredMixin, View):
    def get(self, request):
        if request.user:
            profile_data = Profile.objects.get(username=request.user)
            return render(request, 'profile.html', {'profile_data':profile_data})


@login_required(login_url='login/')
def choice_variable(request):
	return render(request, 'challenge/choice_variable.html')
	
@login_required(login_url='login/')
def get_challenge(request):
    output_query = None
    if request.method == 'POST':
        try:
            search_challenges_by_interests(request.user.interests)
            output_query = search_challenges_by_interests(request.user.interests).all()
            return redirect('successfullyfoundchalleges')
        except NotInterestsFoundError:
            return redirect('challenge')
            print('interests is None')
        except NotMatchesFoundError:
            return redirect('successfullyfoundchalleges')
            print('print all challenge')
    return render(request, 'challenge/intro_challenge.html' )
	
@login_required(login_url='login/')
def get_successfully_found_challeges(request):
    if search_challenges_by_interests(request.user.interests) is not None:
        output_queryset = search_challenges_by_interests(request.user.interests).all()
        print(output_queryset)
    else:
        output_queryset = Challenge.objects.all()
        print(output_queryset)
    context = {
        'challenges':output_queryset
    }
    return render(request, 'challenge/found_challenges.html', context)
	
@login_required(login_url='login/')
def getting_percentage_completed_tasks(request):
	percents = count_percentage_completed_tasks()
	print('per', percents)
	context = {
		'percents':percents
	}
	return render(request, 'notes.html', context)
	
	
class CreateChallenge(CreateView):
    model = Challenge
    form_class = CreateChaklengeForm
    login_url = 'login/'
    template_name = 'challenge/choice_variable.html'
    success_url = '/'
    
    
"""
class StartChallenge(View):
    def get(self, id):
        return Challenge.objects.get(id=id)
        """