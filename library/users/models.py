from django.db import models


from django.contrib.auth.models import AbstractUser
class CustomUser(AbstractUser):
    address=models.CharField(max_length=12,default="")
    phone=models.IntegerField(default=0)

    is_superuser = models.BooleanField(default=False)
    is_user=models.BooleanField(default=False)

    def __str__(self):
        return self.username


class User(models.Model):
    name=models.CharField(max_length=20)
    age=models.IntegerField()
    place=models.CharField(max_length=20)
    gender=models.CharField(max_length=10)
    email=models.CharField(max_length=20)
    def __str__(self):
        return self.name