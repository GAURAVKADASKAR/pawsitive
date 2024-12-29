from home.models import *
from rest_framework.serializers import ModelSerializer,ValidationError
import random

class registrationserializer(ModelSerializer):
    class Meta:
        model=registeration
        fields="__all__"
    
    def create(self, validated_data):
        username=validated_data['username']
        password=validated_data['password']
        address=validated_data['address']
        mobilenumber=validated_data['mobilenumber']
        email=validated_data['email']

        user=User.objects.filter(username=username)
        if user.exists():
            raise ValidationError({'error':'username is already taken'})
        obj1=registeration.objects.filter(email=email)
        
        if obj1.exists():
            raise ValidationError({'error':'email is already taken'})
        

        otp=random_sequence = int(f"{random.randint(0, 9)}{random.randint(0, 9)}{random.randint(0, 9)}{random.randint(0, 9)}{random.randint(0, 9)}")

        obj=registeration.objects.create(
            username=username,
            email=email,
            mobilenumber=mobilenumber,
            address=address,
            password=password,
            otp=otp
        )

        user_obj=User.objects.create(
            username=username
        )
        user_obj.set_password(password)

        obj.save()
        user_obj.save()

        return otp

class Animalserializer(ModelSerializer):
    class Meta:
        model=Animal
        fields="__all__"
    
class Vaccinationserializer(ModelSerializer):
    class Meta:
        model=Vaccination
        fields="__all__"


class Breedserializer(ModelSerializer):
    class Meta:
        model=AnimalBreed
        fields="__all__"
    
class Behaviorserializer(ModelSerializer):
    class Meta:
        model=AnimalBehavior
        fields="__all__"




