from django.urls import path
from . import views

urlpatterns=[
    path('disp_std',views.disp_std),
    path('form',views.form),
]