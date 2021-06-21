from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from ckeditor_uploader.widgets import CKEditorUploadingWidget

from .models import *
from .forms import ProfileForm

"""
class NoteAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model = Note
"""

class ProfileAdmin(UserAdmin):
	model = Profile
	add_form = ProfileForm
	
	fieldsets = (
		*UserAdmin.fieldsets,
		(
			'User profile',
			{
				'fields':(
					'gender',
					'age',
					'phone_number',
					'avatar',
					'interests'
				)
			}
		)
	)

admin.site.register(Profile, ProfileAdmin)
admin.site.register(Note)
admin.site.register(Category)
admin.site.register(Challenge)
admin.site.register(Post)
admin.site.register(Interests)