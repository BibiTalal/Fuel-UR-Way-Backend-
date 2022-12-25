from rest_framework import generics
from  Fuel_UR_Way import serializers
from rest_framework.views import APIView
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView, UpdateAPIView
# from rest_framework.decorators import api_view

from .models import Order
# from .models import Car,FuelType,CarType,Payments,Order


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


class Orderlist(ListAPIView):
    queryset = Order.objects.all()
    serializer_class = serializers.OrderSerializer

class OrderCreate(CreateAPIView):
    serializer_class = serializers.OrderSerializer

class OrderUpdateView(UpdateAPIView):
    queryset = Order.objects.all()
    serializer_class = serializers.OrderUpdateSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'orderId'

class UserOrderslist(ListAPIView):
    # queryset = Order.objects.filter()
    serializer_class = serializers.UserOrdersSerializer
    def get_queryset(self):
        username = self.kwargs['username']
        if username is not None:
            queryset = Order.objects.filter(user=username)
        else:
            queryset = None
        return queryset

class GetOrder(ListAPIView):
    # queryset = Order.objects.filter()
    serializer_class = serializers.OrderSerializer
    def get_queryset(self):
        order_id = self.kwargs['order_id']
        if order_id is not None:
            queryset = Order.objects.filter(id=order_id)
        else:
            queryset = None
        return queryset

class OrderDelete(DestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = serializers.OrderSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'orderId'

# class FuelTypelist(ListAPIView):
#     queryset = FuelType.objects.all()
#     serializer_class = serializers.FuelTypeSerializer

# class FuelTypeCreate(CreateAPIView):
#     serializer_class = serializers.FuelTypeSerializer

# class FuelTypeUpdateView(UpdateAPIView):
#     queryset = FuelType.objects.all()
#     serializer_class = serializers.FuelTypeUpdateSerializer
#     lookup_field = 'id'
#     lookup_url_kwarg = 'fuelId'

# class CarTypelist(ListAPIView):
#     queryset = CarType.objects.all()
#     serializer_class = serializers.CarTypeSerializer

# class CarTypeCreate(CreateAPIView):
#     serializer_class = serializers.CarTypeSerializer

# class CarTypeUpdateView(UpdateAPIView):
#     queryset = CarType.objects.all()
#     serializer_class = serializers.CarTypeUpdateSerializer
#     lookup_field = 'id'
#     lookup_url_kwarg = 'carId'

# class Carlist(ListAPIView):
#     queryset = Car.objects.all()
#     serializer_class = serializers.CarSerializer

# class Carcreate(CreateAPIView):
#     serializer_class = serializers.CarSerializer

# class CarUpdateView(UpdateAPIView):
#     queryset = Car.objects.all()
#     serializer_class = serializers.CarUpdateSerializer
#     lookup_field = 'id'
#     lookup_url_kwarg = 'carId'
#     # def update(self, request, *args, **kwargs):
#     #     instance = self.get_object()
#     #     serializer = self.get_serializer(instance, data=request.data, partial=True)

#     #     if serializer.is_valid():
#     #         serializer.save()
#     #         return Response({"message": "Car updated successfully"},status=HTTP_200_OK)

#     #     else:
#     #         return Response({"message": "failed", "details": serializer.errors},status=HTTP_400_BAD_REQUEST)


# class CarDeleteView(DestroyAPIView):
#     queryset = Car.objects.all()
#     serializer_class = serializers.CarSerializer
#     lookup_field = 'id'
#     lookup_url_kwarg = 'carId'
   


# class Paymentslist(ListAPIView):
#     queryset = Payments.objects.all()
#     serializer_class = serializers.PaymentsSerializer

# class PaymentsCreate(CreateAPIView):
#     serializer_class = serializers.PaymentsSerializer

# class PaymentsUpdateView(UpdateAPIView):
#     queryset = Payments.objects.all()
#     serializer_class = serializers.PaymentsUpdateSerializer
#     lookup_field = 'id'
#     lookup_url_kwarg = 'paymentId'


# class Orderlist(ListAPIView):
#     queryset = Order.objects.all()
#     serializer_class = serializers.OrderSerializer

# class OrderCreate(CreateAPIView):
#     serializer_class = serializers.OrderSerializer

# class OrderUpdateView(UpdateAPIView):
#     queryset = Order.objects.all()
#     serializer_class = serializers.OrderUpdateSerializer
#     lookup_field = 'id'
#     lookup_url_kwarg = 'orderId'