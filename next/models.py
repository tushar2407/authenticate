from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Person(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE, related_name="person")
    age=models.PositiveIntegerField()
    bio=models.CharField(max_length=256)
    def __str__(self):
        #print(self.user.first_name)
        return self.user.username