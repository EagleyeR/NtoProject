from django.contrib.auth.models import User
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Lab(models.Model):
    people = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Лаборатория номер {str(self.pk)}"


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    labs = models.ManyToManyField(Lab)
    phone = PhoneNumberField(null=False, blank=False, unique=True)

    def __str__(self):
        return str(self.user)