import os
from django.shortcuts import render

from trackitadmin.settings import BASE_DIR

class PagesController:
    def index(request):
        directory = os.path.join(BASE_DIR, "templates")
        print("directory", directory)
        return render(request, directory + "/app/pages/index.html")

    def contact(request):
        directory = os.path.join(BASE_DIR, "templates")
        print("directory", directory)
        return render(request, directory + "/app/pages/contact.html")