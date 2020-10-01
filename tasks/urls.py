#urls.py is for the url route (created individually)

from django.urls import path
from . import views      # this will import everything from the views.py file

urlpatterns = [             # this has to be urlpatterns not any other name
    path('', views.index, name='list'),  # this path will call the index func from the views.py
    path('update_task/<str:pk>/', views.updateTask, name="update_task"),  # use str because it works with nums and letters, use the same pk name (from updateTask func in views.py)
    path('delete/<str:pk>/', views.deleteTask, name="delete"),
    
]


