from django.db import models


# Create your models here.

class User(models.Model):
    #Fields 
    name = models.CharField(max_length=120, help_text= 'name of the user')

class Graditude(models.Model):
    #Fields
    date = models.DateField()
    gratitudes = models.TextField(default='')
    user_submitted = models.ForeignKey(User, on_delete=models.CASCADE, default=0)

    def __str__(self):
        return self.gratitudes
