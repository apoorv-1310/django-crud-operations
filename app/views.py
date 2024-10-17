from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from .models import User
import json

'''
Create
'''
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

'''
Read
'''
@api_view(['GET'])
def read(self):
    allUsers =list(User.objects.values()) 
    return JsonResponse({
        'users':allUsers
    })

'''
Update
'''
@api_view(['PUT'])
def update(request,id):
    body = json.loads(request.body.decode("utf-8"))
    print("id",id)
    find = User.objects.filter(id=id)
    if find:
        find.update(
            firstname=body.get('firstname'),
            lastname=body.get('lastname'),
            phoneNo=body.get('phoneNo'),
            )
        return JsonResponse({
            'message':'Updated',
            'find':tuple(find.values())
        })
    else:
        return JsonResponse({
            'message':'Not found',
        },status=404)

'''
Delete
'''
@api_view(['DELETE'])
def delete(request,id):
    User.objects.filter(id=id).delete()
    return JsonResponse({  'message':'Deleted',  },status=200)