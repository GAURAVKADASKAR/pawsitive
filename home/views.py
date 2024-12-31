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

class AddNewPets(APIView):
    def post(self,request):
        if request.session.has_key('username'):
            username=request.session['username']
            animal_name=request.data['Animal_name']
            breed=request.data['Breed']
            vaccination=request.data['vaccination']
            userpk=registeration.objects.get(username=username).id
            aniamlpk=Animal.objects.get(Animal_name=animal_name).id
            breedpk=AnimalBreed.objects.get(Breed=breed).id
            vaccinationpk=Vaccination.objects.get(vaccination=vaccination).id
            obj={
                'username':userpk,
                'vaccination':vaccinationpk,
                'animal_name':aniamlpk,
                'Breed':breedpk,
                'Allergies':request.data['Allergies'],
                'Health_condition':request.data['Health_condition'],
                'Email':request.data['Email'],
                'mobilenumber':request.data['mobilenumber'],
                'age':request.data['age'],
                'Gender':request.data['Gender'],
                'Diet':request.data['Diet']
            }
            serializer=Addpetsserializer(data=obj)
            if serializer.is_valid():
                serializer.save()
                return Response({'status':status.HTTP_200_OK,'message':'success'})
            return Response({'status':status.HTTP_400_BAD_REQUEST,'error':serializer.errors})
        return Response({'status':status.HTTP_401_UNAUTHORIZED,'message':'Login required'})
    

class getallavailablepets(APIView):
    def get(self,request):
        if request.session.has_key('username'):
            obj=Addedpets.objects.filter(Available=True)
            serializer=Addpetsserializer(obj,many=True)
            return Response({'status':status.HTTP_200_OK,'data':serializer.data})
        else:
            return Response({'status':status.HTTP_401_UNAUTHORIZED,'error':'login required'})
    
class getmypets(APIView):
    def get(self,request):
        if request.session.has_key('username'):
            username=request.session['username']
            obj=Addedpets.objects.filter(username__username=username)
            serializer=Addpetsserializer(obj,many=True)
            return Response({'status':status.HTTP_200_OK,'data':serializer.data})
        return Response({'status':status.HTTP_401_UNAUTHORIZED,'error':'login required'})
    
class getpetsbyid(APIView):
    def get(self,request,pets_id):
        obj=Addedpets.objects.get(id=pets_id)
        serializer=Addpetsserializer(obj)
        return Response({'status':status.HTTP_200_OK,'data':serializer.data})


class updatepets(APIView):
    def post(self,request,pets_id):
        if request.session.has_key('username'):
            obj=Addedpets.objects.get(id=pets_id)
            serializer=Addpetsserializer(obj,data=request.data,partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({'status':status.HTTP_200_OK,'message':'success'})
            return Response({'status':status.HTTP_400_BAD_REQUEST,'error':serializer.errors})
        return Response({'status':status.HTTP_401_UNAUTHORIZED,'error':'login required'})

class EnterAdopterdetails(APIView):
    def post(self,request):
       if request.session.has_key('username'):
            username=request.session['username']
            petspk=request.data['pets_detail']
            userid=registeration.objects.get(username=username).id
            data=request.data.copy()
            data['username']=userid
            serializer=PetAdopterserializer(data=data)
            obj=Addedpets.objects.filter(id=petspk).update(Available=False)
            if serializer.is_valid():
                serializer.save()
                return Response({'status':status.HTTP_200_OK,'message':'success'})
            return Response({'status':status.HTTP_400_BAD_REQUEST,'errors':serializer.errors})
       else:
           return Response({'status':status.HTTP_401_UNAUTHORIZED,'error':'login required'})
    


    

        
        


        

    
    


    




    

        

       
