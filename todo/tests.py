from django.test import TestCase, Client
from todo.models import *
from todo.views import *

class NoteTests(TestCase):
    def setUp(self):
        self.client = Client()
    
    def test_get_percents(self):
        response = self.client.get('/', {'progress-bar': '66,7'})