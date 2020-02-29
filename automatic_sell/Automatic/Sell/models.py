
from django.db import models

class Message(models.Model):

   # date = models.DateTimeField(auto_now_add=True)
   content = models.CharField(max_length=255)

# Create your models here.