from django import forms
from .models import Project, Profile, Tag


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        exclude = ['post_date', 'user', ]
        widgets = {
            'tags': forms.CheckboxSelectMultiple(),
        }


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        exclude = ['user', ]
