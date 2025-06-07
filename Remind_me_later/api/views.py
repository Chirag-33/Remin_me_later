from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .serializers import ReminderSerializer
# Create your views here.

class RemindCreateView(APIView):
    def post(self,request):
        serializer = ReminderSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message":"Reminder was created SuccessFully"},status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)