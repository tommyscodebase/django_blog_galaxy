from django.forms import ModelForm
from .models import UserProfile

class UserProfileForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(ModelForm, self).__init__(*args, **kwargs)
        self.fields['about'].widget.attrs.update(
            {'class': 'mt-1 p-2 border w-full rounded-md focus:outline-none focus:ring-emeral-400 focus:border-emerald-300' }
        )
        self.fields['avatar'].widget.attrs.update(
            {'class': 'mt-1 p-2 border w-full rounded-md focus:outline-none focus:ring-emeral-400 focus:border-emerald-300' }
        )
        self.fields['talks_about'].widget.attrs.update(
            {'class': 'mt-1 p-2 border w-full rounded-md focus:outline-none focus:ring-emeral-400 focus:border-emerald-300' }
        )
        

    class Meta:
        model = UserProfile
        fields = ['about', 'avatar', 'talks_about']
        labels = {
            'about': ('Write something about you'),
            'avatar': ('Profile Photo'),
            'talks_about': ('Topics you talks about')
        }