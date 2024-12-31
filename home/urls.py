from django.contrib import admin
from django.urls import path,include
from home.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/',registeruser.as_view()),
    path('Activateuser/',Activateuser.as_view()),
    path('login/',UserLogin.as_view()),
    path('GetAnimalname/',GetAnimalname.as_view()),
    path('GetVaccinationByName/',GetVaccinationByName.as_view()),
    path('GetBreed/',GetBreed.as_view()),
    path('GetBehavior/',GetBehavior.as_view()),
    path('AddNewPets/',AddNewPets.as_view()),
    path('getallavailablepets/',getallavailablepets.as_view()),
    path('getmypets/',getmypets.as_view()),
    path('getpetsbyid/<pets_id>/',getpetsbyid.as_view()),
    path('updatepets/<pets_id>/',updatepets.as_view()),
    path('EnterAdopterdetails/',EnterAdopterdetails.as_view()),
 
]