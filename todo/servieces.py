from django.contrib.auth.models import User
from django.shortcuts import render
from .models import *
from django.db.models import Q
from typing import List


class NotInterestsFoundError(Exception):
    message = 'interests not found'


class NotMatchesFoundError(Exception):
    message = 'mutches not found'

def __init__(self, user):
	profile_user = Profile.objects.get(username=user)

def search_challenges_by_interests(interests:str) -> List[Challenge]:
    if interests is not None:
        matches = Challenge.objects.filter(Q(challenge_name__icontains=interests) | Q(goal__icontains=interests) | Q(describe__icontains=interests))
    if interests is None or matches.first() == None:
        #raise NotMatchesFoundError
        matches = Challenge.objects.all()
        return matches
    print(matches)
    return matches
			
			
def count_percentage_completed_tasks():
	queryset_all_done_tasks = Note.objects.all()
	amount_all_tasks = len(Note.objects.all())
	amount_done_tasks = len(queryset_all_done_tasks.filter(status=1))
	percent = (amount_done_tasks * 100)/ amount_all_tasks
	return "%.1f" % percent