from django.shortcuts import render
from django.http import JsonResponse
from .models import Guest,Movie,Reservations
from .seializers import GuestSeralizer,MovieSerializer,ReservationSerializer
from rest_framework .decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.http import Http404
from rest_framework import mixins,generics
# Create your views here.


def no_model_no__rest(request):
    users = [
        {
            "name":"mohamed yasser",
            "phone":"012010210"
        },
          {
            "name":"nada ahmed",
            "phone":"018914210"
        },
          {
            "name":"gabr tree",
            "phone":"01251450"
        }
    ]
    return JsonResponse(users,safe=False)

def no_rest_model(request):
    data = Guest.objects.all()
    response = {
        "guests":list(data.values())
    }
    return JsonResponse(response,safe=False)


#Function Based Views

@api_view(["GET","POST"])
def guests_list(request):
    if request.method == "GET":
        data = Guest.objects.all()
        seralizer = GuestSeralizer(data,many=True)
        return Response(seralizer.data)
    elif request.method == "POST":

        seralizer = GuestSeralizer(data=request.data)
        if seralizer.is_valid():
            seralizer.save()
            return Response(seralizer.data,status=status.HTTP_201_CREATED)
        return Response(seralizer.data,status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET","PUT","DELETE"])     
def guest_pk(request,pk):
    try:
        guest = Guest.objects.get(pk=pk)
    except Guest.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if(request.method == "GET"):
        seralizer = GuestSeralizer(guest)
        return Response(seralizer.data)
    elif (request.method == "PUT"):
        seralizer = GuestSeralizer(guest,data=request.data)
        if(seralizer.is_valid()):
            seralizer.save()
            return Response(seralizer.data,status=status.HTTP_200_OK)
        return Response(seralizer._errors,status=status.HTTP_400_BAD_REQUEST)
    elif (request.method == "DELETE"):
        guest.delete()
        return Response(status==status.HTTP_204_NO_CONTENT)

#Class Based Views

class CBV_guests(APIView):
    def get(self,request):
        guests = Guest.objects.all(),
        serializer = GuestSeralizer(guests,many=True)
        return Response(serializer.data)
    def post(self,request):
        serializer = GuestSeralizer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)

class CBV_guest_pk(APIView):
    def get_object(self,pk):
        try:
            return Guest.objects.get(pk=pk)
        except Guest.DoesNotExist:
            raise Http404
    def get(self,request,pk):
        guest = self.get_object(pk)
        serializer = GuestSeralizer(guest)
        return Response(serializer.data)
    def put(self,request,pk):
        serializer = GuestSeralizer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,pk):
        self.get_object(pk=pk).delete()
        return Response(status==status.HTTP_204_NO_CONTENT)

#Mixins
# mixins.ListModelMixin =----> return List
# mixins.CreateModelMixin =----> =post to create
# generics.GenericAPIView =----> decorators

class Mixins_list(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
    queryset = Guest.objects.all()
    serializer_class = GuestSeralizer

    def get(self,request):
        return self.list(request)
    def post(self,request):
        return self.create(request)
    
class Mixin_pk(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):
    queryset = Guest.objects.all()
    serializer_class = GuestSeralizer

    def get(self,request,pk):
        return self.retrieve(request)
    def put(self,request,pk):
        return self.update(request)
    def delete(self,request,pk):
        return self.destroy(request)
    
# Generics

class Generics_list(generics.ListCreateAPIView):
    queryset = Guest.objects.all()
    serializer_class = GuestSeralizer

class Generics_pk(generics.RetrieveUpdateDestroyAPIView):
    queryset = Guest.objects.all()
    serializer_class = GuestSeralizer