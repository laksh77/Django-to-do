from django.db import models

# Create your models here.

# first item
class Task(models.Model):
	title = models.CharField(max_length=200)    # the num of characters
	complete = models.BooleanField(default=False)   # set it to false because initially it's not complete
	created = models.DateTimeField(auto_now_add=True)  # whenever an item is created, it will create it automatically

	def __str__(self):
		return self.title





