from . import views
from django.urls import path

urlpatterns=[
    path("save",views.save),
    path("",views.read)
]