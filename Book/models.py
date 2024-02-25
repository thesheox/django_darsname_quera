from datetime import datetime, timezone
from django.utils import timezone
from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)

class Book(models.Model):
    title=models.CharField(max_length=100)
    release_date=models.DateField(default=timezone.now)
    loan_status=models.BooleanField(default=False)
    authors=models.ManyToManyField(Author)
    price=models.PositiveIntegerField(default=2000)

class Profile(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)

class Library(models.Model):
    number=models.PositiveIntegerField()

class Personel(models.Model):
    class Gender(models.TextChoices):
        MALE="m","Male"
        FEMALE="f","Female"
    gender = models.CharField(max_length=1, choices=Gender.choices, default=Gender.MALE)  # Correct
    profile=models.OneToOneField(Profile, on_delete=models.CASCADE)
    library=models.ForeignKey(Library, on_delete=models.CASCADE)

# from django.db import models
# class Factory(models.Model):
#     name = models.CharField(max_length=10)
#
# class Car(models.Model):
#     name = models.CharField(max_length=10)
#     color = models.CharField(max_length=10, choices=[('b', 'Black'), ('w', 'White')])
#     factory = models.ForeignKey(Factory, on_delete=models.CASCADE)
#     price = models.IntegerField()



from django.db import models


# class User(models.Model):
#
#     name = models.CharField(max_length=10)
#     password = models.CharField(max_length=10)
#     score = models.IntegerField()
#     def change_name(self, new_name):
#         self.name=new_name
#
#     def change_password(self, new_password):
#         self.password=new_password
#
#     def change_score(self, x):
#         self.score=self.score+x
#
#     def __str__(self):
#         return self.name
