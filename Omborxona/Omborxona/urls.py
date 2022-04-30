from django.contrib import admin
from django.urls import path
from mainapp.views import ProductAPIView, ClientAPIView, StatsAPIView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('get-token/', TokenObtainPairView.as_view()),
    path('upd-token/', TokenRefreshView.as_view()),

    path('products/', ProductAPIView.as_view()),
    path('products/<int:pk>/', ProductAPIView.as_view()),

    path('clients/', ClientAPIView.as_view()),
    path('clients/<int:pk>/', ClientAPIView.as_view()),

    path('stats/', StatsAPIView.as_view()),
]
