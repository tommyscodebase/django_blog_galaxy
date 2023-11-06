from django import forms
from .models import Comment, Post

class PostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(forms.ModelForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update(
            {'class': 'mt-1 p-2 border w-full rounded-md focus:outline-none focus:ring-emeral-400 focus:border-emerald-300' }
        )
        self.fields['body'].widget.attrs.update(
            {'class': 'mt-1 p-2 border w-full rounded-md focus:outline-none focus:ring-emeral-400 focus:border-emerald-300' }
        )
        self.fields['image'].widget.attrs.update(
            {'class': 'mt-1 p-2 border w-full rounded-md focus:outline-none focus:ring-emeral-400 focus:border-emerald-300' }
        )
        

    class Meta:
        model = Post
        fields = ['title', 'body', 'image']
        labels = {
            'about': ('Write something about you'),
            'avatar': ('Profile Photo'),
            'talks_about': ('Topics you talks about')
        }


class CommentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(forms.ModelForm, self).__init__(*args, **kwargs)
        self.fields['body'].widget.attrs.update(
            {'class': 'mt-1 p-2 border w-full rounded-md focus:outline-none focus:ring-emeral-400 focus:border-emerald-300' }
        )
        
        
    class Meta:
        model = Comment
        fields = ['body']
        labels = {
            'text': ('Comment'),
        }



class EmailPostForm(forms.Form):
    name = forms.CharField(max_length=50, widget=forms.TimeInput(
        attrs={'class':'mt-1 p-2 border w-full rounded-md focus:outline-none focus:ring-emerald-400 focus:border-emerald-300'}
    ))
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={'class':'mt-1 p-2 border w-full rounded-md focus:outline-none focus:ring-emerald-400 focus:border-emerald-300'}
    ))
    to = forms.EmailField(widget=forms.EmailInput(
        attrs={'class':'mt-1 p-2 border w-full rounded-md focus:outline-none focus:ring-emerald-400 focus:border-emerald-300'}
    ))
    comments = forms.CharField(required=False, widget=forms.Textarea(
        attrs={'class':'mt-1 p-2 border w-full rounded-md focus:outline-none focus:ring-emerald-400 focus:border-emerald-300', 'rows':'5'}
    ))