from django.db import models

class User (models.Model):
    username = models.CharField(max_length=150, unique=False , verbose_name='Prenom')