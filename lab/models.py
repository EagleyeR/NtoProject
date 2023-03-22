from django.contrib.auth.models import User
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Lab(models.Model):
    people = models.ForeignKey(User, on_delete=models.CASCADE, name="Люди в лаборатории")

    bar = models.IntegerField(default=0)  # Давление
    temperature = models.IntegerField(default=0)  # Температура
    humidity = models.IntegerField(default=0)  # Влажность
    heighWaterFirst = models.IntegerField(default=0)  # Объем в первой колбе
    heighWaterSecond = models.IntegerField(default=0)  # Объем во второй колбе
    lux = models.IntegerField(default=0)  # Яркость света
    co2 = models.IntegerField(default=0)  # Уровень углекислого газа
    emission_pr = models.IntegerField(default=0)  # Уровень других газов
    countWater = models.IntegerField(default=0)  # Сколько воды прошло
    pumpAlert = models.BooleanField(default=False)  # Переполнение, тревога
    otherGasAlert = models.BooleanField(default=False)  # Тревога всех газов
    co2Alert = models.BooleanField(default=False)  # Углекислый гах, тревога
    door = models.BooleanField(default=False)  # Дверь
    start_lab = models.BooleanField(default=False)  # Работает ли лаборатория
    went = models.BooleanField(default=False)  # Работает ли вентилятор
    window = models.BooleanField(default=False)  # Окно
    went_speed = models.BooleanField(default=False)  # Скорость вентилятора
    gyroscope = models.IntegerField(default=0)  # Гироскоп
    light_level = models.IntegerField(default=0)  # Освещенность в комнате

    # Цвета жидкости
    all_color = [("Gold", "Yellow"), ("Green", "Green"), ("Blue", "Blue"), ("Black", "Black")]
    light_request = models.CharField(max_length=6, choices=all_color, blank=True)  # Запрошенный цвет

    RGB = models.CharField(max_length=11, blank=True)  # РГБ, значение жидкости
    color = models.CharField(max_length=6, choices=all_color, blank=True)  # Цвет жидкости

    def __str__(self):
        return f"Лаборатория номер {str(self.pk)}"


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    labs = models.ManyToManyField(Lab)
    phone = PhoneNumberField(null=False, blank=False, unique=True)

    def __str__(self):
        return str(self.user)
