from django.shortcuts import render
from rest_framework.decorators import api_view
from django.http import JsonResponse
from .v1.services.WelcomeService import WelcomeService

@api_view(['GET'])
def welcome(request):
    welcome_service = WelcomeService()
    welcome_message = welcome_service.get_welcome_message()
    return JsonResponse({"message": welcome_message})