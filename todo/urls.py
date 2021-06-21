from django.urls import path, include
from django.urls import reverse
from . import views
from .views import *


urlpatterns = [
	path('login/', views.login_user, name="login"),
	path('logout/', views.logout_user, name="logout"),
    path('', views.NotesList.as_view(), name='notes'),
    path('create/', views.CreateNote.as_view(), name="create"),
    path('edit/<int:id>/', views.NoteUpdate, name="edit"),
    path('delete/<int:pk>/', views.NoteDelete.as_view(), name="delete"),
    path('registration/', views.register, name="registration"),
    path('profile/', views.ProfileView.as_view(), name="profile"),
    path('intro_challenge/', views.get_challenge, name="intro"),
    path ('choice_variable/', views.CreateChallenge.as_view(), name='challenge'),
    path('found_challenges/', views.get_successfully_found_challeges, name='successfullyfoundchalleges'),
    path('blog/', views.BlogView.as_view(), name="blog"),
    #path('start_challenge/<int:id>/', views.StartChallenge.as_view(), name="start_challege")
]