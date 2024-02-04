from django.db import models

# Create your models here.
from django.db import models

class UserDetails(models.Model):
    firstname=models.CharField(max_length=255)
    lastname=models.CharField(max_length=255)
    dob=models.DateField()
    email=models.EmailField()


    def __str__(self):
        return self.firstname