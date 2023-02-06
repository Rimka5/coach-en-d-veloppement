from django.db import models

class Profil (models.Model):
    nom=models.fields.CharField(max_length=100)
    date_de_naissance=models.fields.CharField(max_length=100)
