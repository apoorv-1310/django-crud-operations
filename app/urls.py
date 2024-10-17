from . import views
from django.urls import path

urlpatterns=[
    path("save",views.save),
    path("",views.read),
    path("update/<int:id>",views.update),
    path("delete/<int:id>",views.delete)
]