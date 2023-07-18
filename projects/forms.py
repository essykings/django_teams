from django.forms import ModelForm
from .models import Task,Project

from django.forms import DateInput

class TaskForm(ModelForm):
  class Meta:
      model =Task
      fields ='__all__'
      widgets = {'due_date': DateInput( format=('%Y-%m-%d'),
               attrs={'type': 'date' }),
               }

class ProjectForm(ModelForm):
  class Meta:
      model =Project
