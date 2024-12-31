from django.db import models
from django.contrib.auth.models import User


class registeration(models.Model):
    User=models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)
    username=models.TextField()
    email=models.EmailField(unique=True)
    address=models.TextField()
    mobilenumber=models.TextField()
    password=models.TextField()
    otp=models.PositiveIntegerField(null=True)
    is_Active=models.BooleanField(default=False)

    def __str__(self):
        return self.username

class Animal(models.Model):
    Animal_name=models.CharField(max_length=20)

    def __str__(self):
        return self.Animal_name

class Vaccination(models.Model):
    Animal=models.ForeignKey(Animal,on_delete=models.SET_NULL,null=True,blank=True)
    vaccination=models.CharField(max_length=30)
    def __str__(self):
        return self.vaccination

class AnimalBreed(models.Model):
    Animal=models.ForeignKey(Animal,on_delete=models.SET_NULL,null=True,blank=True)
    Breed=models.CharField(max_length=20)

    def __str__(self):
        return self.Breed    

class AnimalBehavior(models.Model):
    Animal=models.ForeignKey(Animal,on_delete=models.SET_NULL,null=True,blank=True)
    Behavior=models.CharField(max_length=20)

    def __str__(self):
        return self.Behavior

class Addedpets(models.Model):
    username=models.ForeignKey(registeration,on_delete=models.SET_NULL,null=True,blank=True)
    animal_name=models.ForeignKey(Animal,on_delete=models.SET_NULL,null=True,blank=True)
    vaccination=models.ForeignKey(Vaccination,on_delete=models.SET_NULL,null=True,blank=True)
    Breed=models.ForeignKey(AnimalBreed,on_delete=models.SET_NULL,null=True,blank=True)
    age=models.PositiveBigIntegerField()
    Gender=models.CharField(max_length=20)
    Diet=models.TextField()
    AnimalPhoto=models.FileField(upload_to='Animal_image',default='')
    mobilenumber=models.TextField()
    Email=models.TextField()
    Health_condition=models.TextField()
    Allergies=models.TextField()
    Available=models.BooleanField(default=True)
    def __str__(self):
        return self.Email

class PetAdopter(models.Model):
    username=models.ForeignKey(registeration,on_delete=models.SET_NULL,null=True,blank=True)
    pets_detail=models.ForeignKey(Addedpets,on_delete=models.SET_NULL,null=True,blank=True)
    name=models.CharField(max_length=50)
    gender=models.CharField(max_length=20)
    contact_email=models.CharField(max_length=20,default='')
    contact_number=models.TextField(default='')
    address=models.TextField()
    occupation=models.TextField()
    pet_experiance=models.TextField()
    another_pets=models.BooleanField(default=False)
    permissionTovisit=models.BooleanField(default=True)
    final_permission=models.BooleanField(default=True)

    def __str__(self):
        return self.name

