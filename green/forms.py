from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):
    content = forms.CharField(label='', widget=forms.Textarea(attrs={'rows': 10}))
    class Meta:
        model = Post
        fields = ['category', 'content', 'image', 'video']
        widgets = {
            'image': forms.FileInput(attrs={'class': 'form-control-file'}),
            'video': forms.FileInput(attrs={'class': 'form-control-file'}),
        }

class CommentForm(forms.ModelForm):
    content = forms.CharField(label='', widget=forms.Textarea(attrs={'rows': 3}))
    class Meta:
        model = Comment
        fields = ['content']