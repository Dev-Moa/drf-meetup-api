from django.shortcuts import render
from rest_framework.views import APIView
from api.models import MeetUp
from api.serializers import MeetUpSerializer
from rest_framework.response import Response
# Create your views here.


class MeetUpAPIView(APIView):
    def get(self,request):
        meetups = MeetUp.objects.all()
        serializer = MeetUpSerializer(meetups,many=True)
        return Response(serializer.data)
    def post(self,request):
        data = request.data
        serializer = MeetUpSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data,status=201)
        return Response(serializer.errors,status=400)