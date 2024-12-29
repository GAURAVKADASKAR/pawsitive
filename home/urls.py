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
    path('GetBehavior/',GetBehavior.as_view())
 
]