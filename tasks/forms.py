# this represents the model (form representation of the model)
# this will create the form fields for us and we can import it into the template

from django import forms
from django.forms import ModelForm

# class based form
from .models import *  # imports all the models in models.py file

# create a model form (modelname and form)
class TaskForm(forms.ModelForm):
    title= forms.CharField(widget= forms.TextInput(attrs={'placeholder':'Add new task...'})) # set the placeholder value 
    
    class Meta:     # Meta needs at least 2 values
        model = Task    # the model we are creating a form for
        fields = '__all__'   # what fields are we allowing in the form from the model (all)





