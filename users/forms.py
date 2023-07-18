from .models import Profile
from django.forms import ModelForm

class ProfileForm(ModelForm):
    class Meta:
        model =Profile
        fields = ['name','email','bio','photo']
