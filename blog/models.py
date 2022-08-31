from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Post(models.Model):
  title = models.CharField(max_length=100)
  content = models.TextField()
  date_posted = models.DateTimeField(default=timezone.now) # auto_now=True updates everytime auto_now_add=True set after first time adding 
  author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL) #deleting user doesn't delete posts
  #author = models.ForeignKey(User, on_delete=models.CASCADE) #deleteing user deletes posts

  def __str__(self):
    return self.title
