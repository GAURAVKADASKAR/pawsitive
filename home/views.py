from django.shortcuts import render
from home.serializer import *
from rest_framework import authentication
from rest_framework.decorators import APIView
from django.conf import settings
from django.core.mail import send_mail
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate


class registeruser(APIView):
    def post(self,request):
        serializer=registrationserializer(data=request.data)
        if not serializer.is_valid():
            return Response({'status':status.HTTP_400_BAD_REQUEST,'error':serializer.errors})
        
        otp=serializer.save()

        subject = "Account Verification for Pawsitive"
       
        message = f"""Dear User,

        Thank you for registering with Pawsitive, our initiative for pet donation and receiving.

        To complete the registration process and ensure the security of your account, please verify your identity using the following OTP:

        **{otp}**

        If you are unable to use the OTP above, please contact us for assistance.

        Once your OTP has been verified, you will gain full access to our platform and its features, allowing you to connect with pet donors or find loving homes for pets in need.

        If you did not register with Pawsitive, please ignore this email.

        Thank you for choosing Pawsitive. If you have any questions or need further assistance, please don't hesitate to contact us at pawsitive.support@gmail.com.

        Best regards,  
        The Pawsitive Team
        """

        from_email=settings.EMAIL_HOST_USER
        user=request.data['email']
        recipient_list=[user]
        send_mail(subject,message,from_email,recipient_list)
        return Response({'status':status.HTTP_200_OK,'message':'success'})



class Activateuser(APIView):
    def post(self,request):
        otp=request.data['otp']
        obj=registeration.objects.filter(otp=otp).update(is_Active=True)
        return Response({'status':status.HTTP_200_OK,'message':'success'})


class UserLogin(APIView):
    def post(self,request):
        username=request.data['username']
        password=request.data['password']
        obj=registeration.objects.filter(username=username)
        if obj.exists():
            obj=registeration.objects.filter(username=username).first()
            if obj.is_Active:
                user=authenticate(username=username,password=password)
                if user is None:
                    return Response({'status':status.HTTP_400_BAD_REQUEST,'error':'Invalid username or password'})
                else:
                    request.session['username']=username
                    return Response({'status':status.HTTP_200_OK,'message':'login'})
            else:
                return Response({'status':status.HTTP_401_UNAUTHORIZED,'message':'User is not verified'})
        else:
            return Response({'status':status.HTTP_400_BAD_REQUEST,'error':'Invalid username or password'})
        

class GetAnimalname(APIView):
    def get(self,request):
        obj=Animal.objects.all()
        serializer=Animalserializer(obj,many=True)
        return Response({'status':status.HTTP_200_OK,'data':serializer.data})


class GetVaccinationByName(APIView):
    def post(self,request):
        animalname=request.data['Animal']
        obj=Vaccination.objects.filter(Animal__Animal_name=animalname)
        serializer=Vaccinationserializer(obj,many=True)
        return Response({'status':status.HTTP_200_OK,'data':serializer.data})


class GetBreed(APIView):
    def post(self,request):
        animalname=request.data['Animal']
        obj=AnimalBreed.objects.filter(Animal__Animal_name=animalname)
        serializer=Breedserializer(obj,many=True)
        return Response({'status':status.HTTP_200_OK,'data':serializer.data})

class GetBehavior(APIView):
    def post(self,request):
        animalname=request.data['Animal']
        obj=AnimalBehavior.objects.filter(Animal__Animal_name=animalname)
        serializer=Behaviorserializer(obj,many=True)
        return Response({'status':status.HTTP_200_OK,'data':serializer.data})


    




    

        

       
