from django.urls import path
from . import views

urlpatterns= [
    path('',views.webDev),
    path('AboutUs',views.AboutUs, name="index"),
    path('Bank',views.Bank)

]