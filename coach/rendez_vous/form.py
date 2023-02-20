from django import forms
from.models import rendez_vous

class rendez_voustForm(forms.ModelForm):
    model = rendez_vous
    fields = ("date", 'objet_seance')