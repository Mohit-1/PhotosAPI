from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from photos.serializers import PhotoSerializer, PhotoDataSerializer, GroupSerializer
from photos.models import Photo, Group
from rest_framework import generics 

# Create your views here.
class ListGroups(generics.ListAPIView):
    permission_classes = (IsAuthenticated, )
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class ListPhotoForGroup(APIView):
    permission_classes = (IsAuthenticated, )

    def get(self, request, gid):
        group = Group.objects.get(name=gid)
        queryset = Photo.objects.filter(group=group)
        serializer = PhotoSerializer(queryset, many=True)
        return Response(serializer.data)

class PhotoDetails(APIView):
    permission_classes = (IsAuthenticated, )

    def get(self, request, pid):
        photo = Photo.objects.get(pid=pid)
        serializer = PhotoDataSerializer(photo)
        return Response(serializer.data)
