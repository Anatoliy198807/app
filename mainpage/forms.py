from django import forms
from .models import Post, ProjectFile

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'text']
        labels = {
            'title':'Заголовок поста',
            'text':'Текст поста'
        }       
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'text': forms.Textarea(attrs={'class':'form-control'})
        }

class ProjectFileForm(forms.ModelForm):
    class Meta:
        model = ProjectFile
        fields = ['name', 'text', 'file', 'desing_project' ]
        labels = {
            'name':'Название изображения',
            'text':'Описание',
            'desing_project':'проект'
        }       
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'text': forms.Textarea(attrs={'class':'form-control'}),
            'desing_project': forms.TextInput(attrs={'class':'form-control'}),
        }