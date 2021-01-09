from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView


class ping(APIView):
    def get(self, request):
        return Response({"status": "OK"})

