from django.shortcuts import render
#from facebook import GraphAPI 
import facebook as fb
from rest_framework import permissions
from rest_framework.authtoken.serializers import AuthTokenSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import PostSerializer
from django.conf import settings
from PIL import Image
import requests


# Create your views here.
class PostViews(APIView):
    def post(self, request):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            access_token="EAAGMrJGXYtYBACQwzvVNHYVKdm33vs17ts0ZAg0ynF09IjHprhQURZCtWoJtl80Oqbh6LxZAFl6CdjUCWehCDAJ9OVWVeANbK0bBTTZCvwZCutkyXgdfVlZAUCL826NvZBdZB0814tE8kwusdGcJggsMtpeFvZC3NqCKMBAB2iDrONlWLzARUPcJx07OAKrZBd79QZD"
            asafb=fb.GraphAPI(access_token)
            asafb.put_object("me","feed",message="this is automated post facebookss1")
            asafb.get_object("110171264960518_113190911325220")
            asafb.put_photo(open(serializer.data['photo'],"rb"), message=serializer.data['facebook_post'])
    
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)   
