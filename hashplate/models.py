from django.db import models

class UserInput(models.Model):
    field_one = models.CharField(max_length=100)
    field_two = models.CharField(max_length=100)

class HashedData(models.Model):
    plate = models.CharField(max_length=8)
    hashed_data = models.CharField(max_length=100)
