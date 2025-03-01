from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Userprofile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)

    # additional fields
    phone = models.BigIntegerField()
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zipcode = models.IntegerField()
    image = models.ImageField(upload_to='userimg/',blank=True,null=True)
    