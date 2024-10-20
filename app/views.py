from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from .models import User
import json


def index():
    print('hiio')