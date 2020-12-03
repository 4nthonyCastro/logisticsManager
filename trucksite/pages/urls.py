from django.urls import path, include
from . import views

app_name = 'pages'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('about/', views.AboutView.as_view(), name='about'),
     # path('pages/', views.products, name='products'),
]
