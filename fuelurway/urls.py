"""fuelurway URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Fuel_UR_Way import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    path("signin/", views.SigninView.as_view(), name="signin"),
    path("register/", views.RegisterView.as_view(), name="register"),
    #Order
    path('list/order/', views.Orderlist.as_view(), name='orderList'),
    path('create/order/', views.OrderCreate.as_view(), name='create-order'),
    path('edit/order/<int:orderId>/', views.OrderUpdateView.as_view(), name='edit-order'),
    path('userList/order/<str:username>/', views.UserOrderslist.as_view(), name='userOrdersList'),
    path('get/order/<int:order_id>/', views.GetOrder.as_view(), name='get_order'),
    path('Delete/order/<int:orderId>/', views.OrderDelete.as_view(), name='delete-order'),
    
#     #Car
#     path('list/cars/', views.Carlist.as_view(), name='carList'),
#     path('create/car/', views.Carcreate.as_view(), name='create-car'),
#     path('edit/car/<int:carId>/', views.CarUpdateView.as_view(), name='edit-car'),
#     path('delete/car/<int:carId>/', views.CarDeleteView.as_view(), name='delete-car'),
#     #FuelType
#     path('list/fuelType/', views.FuelTypelist.as_view(), name='fuelTypeList'),
#     path('create/fuelType/', views.FuelTypeCreate.as_view(), name='create-fuelType'),
#     path('edit/fuelType/<int:fuelId>/', views.FuelTypeUpdateView.as_view(), name='edit-fuelType'),
#     #CarType
#     path('list/carType/', views.CarTypelist.as_view(), name='carTypeist'),
#     path('create/carType/', views.CarTypeCreate.as_view(), name='create-carType'),
#     path('edit/carType/<int:carId>/', views.CarTypeUpdateView.as_view(), name='edit-carType'),
#     #Payments
#     path('list/payments/', views.Paymentslist.as_view(), name='paymentsList'),
#     path('create/payments/', views.PaymentsCreate.as_view(), name='create-payments'),
#     path('edit/payments/<int:paymentId>/', views.PaymentsUpdateView.as_view(), name='edit-payments'),
#     #Order
#     path('list/order/', views.Orderlist.as_view(), name='orderList'),
#     path('create/order/', views.OrderCreate.as_view(), name='create-order'),
#     path('edit/order/<int:orderId>/', views.OrderUpdateView.as_view(), name='edit-order'),

]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
