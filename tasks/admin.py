from django.contrib import admin


# Register your models here.

from .models import *  # imports everything from the models file

admin.site.register(Task)   # this registers the task func from models.py, then you can see it in the admin page
