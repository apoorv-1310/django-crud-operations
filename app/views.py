from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from .models import User
import json

# Create your views here.
@api_view(['POST'])
def save(request):
    body = json.loads(request.body.decode("utf-8"))
    print(body.get('firstname'))
    User.objects.create(
        firstname=body.get('firstname'),
        lastname=body.get('lastname'),
        phoneNo=body.get('phoneNo')
        )
    return JsonResponse(body)

@api_view(['GET'])
def read(self):
    allUsers =list(User.objects.values()) 
    return JsonResponse({
        'users':allUsers
    })

