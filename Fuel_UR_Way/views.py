from rest_framework import generics
from  Fuel_UR_Way import serializers
from rest_framework.views import APIView
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView, UpdateAPIView
# from rest_framework.decorators import api_view

from .models import Car


class RegisterView(generics.CreateAPIView):
    serializer_class = serializers.RegisterSerializer


class SigninView(APIView):
    serializer_class = serializers.SigninSerializer

    def post(self, request):
        data = request.data
        serializer = serializers.SigninSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            valid_data = serializer.data
            return Response(valid_data, status=HTTP_200_OK)
        else:
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


class Carlist(ListAPIView):
    queryset = Car.objects.all()
    serializer_class = serializers.CarSerializer

class Carcreate(CreateAPIView):
    serializer_class = serializers.CarSerializer

class CarUpdateView(UpdateAPIView):
    queryset = Car.objects.all()
    serializer_class = serializers.CarUpdateSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'carId'
    # def update(self, request, *args, **kwargs):
    #     instance = self.get_object()
    #     serializer = self.get_serializer(instance, data=request.data, partial=True)

    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response({"message": "Car updated successfully"},status=HTTP_200_OK)

    #     else:
    #         return Response({"message": "failed", "details": serializer.errors},status=HTTP_400_BAD_REQUEST)


class CarDeleteView(DestroyAPIView):
    queryset = Car.objects.all()
    serializer_class = serializers.CarSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'carId'
    # def delete(self, request, *args, **kwargs):
    #     instance = self.get_object()
    #     serializer = self.get_serializer(instance, data=request.data, partial=True)

    #     if serializer.is_valid():
    #         serializer.de
    #         return Response({"message": "Car deleted successfully"},status=HTTP_200_OK)

    #     else:
    #         return Response({"message": "failed", "details": serializer.errors},status=HTTP_400_BAD_REQUEST)
    

