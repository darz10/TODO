from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from ckeditor_uploader.fields import RichTextUploadingField


GENDER = (
	('male', 'male'),
	('female', 'female')
)


class Profile(AbstractUser):
	# расширенная модель регистрации пользователя User
	gender = models.CharField(max_length=6, choices=GENDER, default='male')
	age = models.PositiveSmallIntegerField(blank=True, null=True)
	phone_number = models.CharField(max_length=12, blank=True, null=True)
	avatar = models.ImageField(upload_to='media/avatar', blank=True, null=True)
	interests = models.ForeignKey('Interests',on_delete=models.CASCADE, blank=True, null=True)
	
	def __str__(self):
		return self.username
			
			
class Interests(models.Model):
	interests = models.CharField(max_length=50, blank=True, null=True)
	
	def __str__(self):
		return self.interests


class Note(models.Model):
	# модель создания заметок
	title = models.CharField(max_length=100)
	content = RichTextUploadingField(blank=True, null=True)
	category = models.ForeignKey('Category', on_delete=models.CASCADE, blank=True, null=True)
	image = models.ImageField(upload_to='media/note', blank=True, null=True)
	status = models.BooleanField(verbose_name='Done', default=False)
	time_add = models.DateTimeField(default=timezone.now)
	
	def __str__(self):
		return self.title
		
	class Meta:
		ordering = ['-time_add']
	
		

class Category(models.Model):
	category = models.CharField(max_length=100)
	
	def __str__(self):
		return self.category
		

class Challenge(models.Model):
	challenge_name = models.CharField(max_length=50)
	goal = models.CharField(max_length=50)
	describe = models.TextField(max_length=200)
	deadline = models.DateTimeField(default=timezone.now)
	benefit = models.CharField(max_length=50)#польза от челенджа
	
	def __str__(self):
		return self.challenge_name
		

class Post(models.Model):
	title_post = models.CharField(max_length=50)
	post = RichTextUploadingField(blank=True, null=True)
	photo = models.ImageField(upload_to='media/blog', blank=True, null=True)
	time_creation = models.DateTimeField(default=timezone.now)
	category_post= models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
	comment = models.TextField(max_length=150, default="", blank=True, null=True)

	def __str__(self):
		return self.title_post