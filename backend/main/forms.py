from django import forms
from main.models import Resume, Skill, Education, PreviousJob

class ResumeForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = ['profile_image', 'success_summary']

class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = ['name']

class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = ['school_name', 'degree', 'start_date', 'end_date', 'description']
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
        }

class PreviousJobForm(forms.ModelForm):
    class Meta:
        model = PreviousJob
        fields = ['company', 'position', 'start_date', 'end_date', 'description']
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
        }
