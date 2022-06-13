
from django.db import models
# Create your models here.
class User(models.Model):
        regNo = models.CharField(unique=True,max_length=100)
        name = models.CharField(max_length=100)
        email = models.EmailField()
        mobile = models.CharField(null=True,max_length=100)
        created_at = models.DateTimeField(auto_now=True)