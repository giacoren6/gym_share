from django.shortcuts import render
from rest_framework import APIView
from rest_framework.response import Response
from .models import Profile

class profile_list(APIView):
    def get(self, request):
        profiles = Profile.objects.all()
        return Response({"profiles": profiles})




