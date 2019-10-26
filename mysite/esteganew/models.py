from django.db import models

class post(models.Model):
    """docstring for post."""
    x = 100 #value given by the max length method
    messaje = models.CharField(max_length = x)
    new_name = models.CharField(max_length = 20)    
