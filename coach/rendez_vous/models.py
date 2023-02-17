from django.db import models
from coach_rdv.models import User

class rendez_vous(models.Model):
    date = models.DateField()
    coach = models.ForeignKey(User, on_delete=models.CASCADE, related_name='rendez_vous')
    client = models.ForeignKey(User, on_delete=models.CASCADE, related_name='mes_rendez_vous')
    objet_seance = models.CharField(max_length=200)

class Meta:
    verbose_name = "Rendez_vous"
    verbose_name_plural = ("Rendez_vous")