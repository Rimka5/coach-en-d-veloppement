from .models import rendez_vous
from django.shortcuts import render, redirect
# from django.contrib.auth.decorators import login_required
# from django.forms import ModelForm, ValidationError
# from django.utils import timezone
# from datetime import timedelta



# def prendre_rdv(request):
#     if request.method == 'POST':
#           # Récupération des données du formulaire
#         date = request.POST['date']
#         heure = request.POST['heure']
#         objet_seance = request.POST['objet_seance']
        
#         # Vérification que le coach est disponible à cette date et heure
#         rdv_existant = rendez_vous.objects.filter(date=date, heure=heure).first()
#         if rdv_existant is not None:
#             message = "Le coach est déjà occupé à cette date et heure."
#             return render(request, 'prendre_rdv.html', {'message': message})
        
#         # Création d'un nouveau rendez-vous
#         rdv = rendez_vous(date=date, heure=heure, objet_seance=objet_seance, client=request.user)
#         rdv.save()
        
#         # Redirection vers la page de succès
#         # return redirect('success')
#     else:
#         return render(request, 'prendre_rdv.html')





