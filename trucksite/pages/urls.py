from django.urls import path, include
from . import views

app_name = 'pages'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('services/', views.ServicesView.as_view(), name='services'),
    path('products/', views.ProductsView.as_view(), name='products'),
]
