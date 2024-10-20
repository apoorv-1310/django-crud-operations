from app.apis.main import APIController
from app.views.page import PagesController
# from app.views import PagesController
from . import views
from django.urls import path


urlpatterns=[
    path("api/save", APIController.save),
    path("api/",APIController.read),
    path("api/update/<int:id>",APIController.update),
    path("api/delete/<int:id>",APIController.delete),
    path("views/",PagesController.index)
]