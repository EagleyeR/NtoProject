from django.contrib.auth.models import User
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Lab(models.Model):
    people = models.ForeignKey(User, on_delete=models.CASCADE, name="Люди в лаборатории")
    temperature = models.CharField(max_length=3, name="Температура")
    humidity = models.CharField(max_length=5, name="Влажность")
    heighWaterFirst = models.CharField(max_length=3, name="Объем в первой колбе")
    heighWaterSecond = models.CharField(max_length=3, name="Объем во второй колбе")
    lux = models.CharField(max_length=5, name="Яркость света")
    co2 = models.CharField(max_length=5, name="Уровень углекислого газа")
    emission_pr = models.CharField(max_length=5, name="Уровень других газов")
    countWater = models.CharField(max_length=3, name='Сколько воды прошло')
    pumpAlert = models.BooleanField(default=False, name="Переполнение, тревога")
    otherGasAlert = models.BooleanField(default=False, name="Тревога всех газов")
    co2Alert = models.BooleanField(default=False, name="Углекислый гах, тревога")
    door = models.BooleanField(default=False, name="Дверь")
    start_lab = models.BooleanField(default=False, name="Работает ли лаборатория")
    went = models.BooleanField(default=False, name="Работает ли вентилятор")
    window = models.BooleanField(default=False, name="Окно")


    RGB = models.CharField(max_length=11, name="РГБ, значение жидкости")
    color = models.CharField(max_length=6, name="Цвет жидкости")


    def __str__(self):
        return f"Лаборатория номер {str(self.pk)}"


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    labs = models.ManyToManyField(Lab)
    phone = PhoneNumberField(null=False, blank=False, unique=True)

    def __str__(self):
        return str(self.user)