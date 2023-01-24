from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import status
from rest_framework.authentication import TokenAuthentication

from profiles_api import serializers
from profiles_api import models
from profiles_api import permissions


class HelloAPIView(APIView):
    """Test API View"""
    serializer_class=serializers.HelloSerializer

    def get(self,request,format=None):
        """Returns a list of API features"""
        an_apiview=[
            'Uses HTTP Methods as function (get , post ,patch,put , delete)',
            'Is similar to a traditionl Django view',
            'Gives you the m,ost control over your application logic',
            'Is mapped manually to URLS',
        ]

        return Response({'message':'Hello','an API View':an_apiview})


def post(self,request):
    """Create a hello message with our name"""
    serializer= self.serializer_class(data = request.data)


    if serializer.is_valid():
        name = serializer.validated_data.get('name')
        message = f'Hello {name}!'
        return Response({'message':message})
    else:
        return Response(serializer.errors,
        status = status.HTTP_400_BAD_REQUEST
        )



class HelloViewSet(viewsets.ViewSet) :
    """Test API Viesets"""
    serializer_class = serializers.HelloSerializer

    def list(self,request):
        """return a hello message"""
        a_viewset = [
            'Uses actions list, create , retrieve ,update, partial_update',
            'automatically maps to URLS using Routers',
            'Provides more finctionality with less code',
        ]

        return Response({'message':'Hello','a_viewset':a_viewset})


    def create(self,request):
        """Create a new hello message"""
        serializer = self.serializer_class(data = request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}!'
            return Response({'message':message})
        else:
            return Response(
                serializer.errors,
                status = status.HTTP_400_BAD_REQUEST
            )


    def retrieve(self,request,pk=None):
        """Handle getting an object by its ID"""
        return Response({'http_method':'GET'})


    def update(self,request,pk=None):
        """Handle updating an object"""
        return Response({'http_method':'PUT'})


    def partial_update(self,request,pk=None):
        """Handle updating part of an object"""
        return Response({'http_method':'PATCH'})


    def destroy(self,request,pk=None):
        """Handle removing an object"""
        return Response({'http_method':'DELETE'})


class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating and updfating profiles"""
    serializer_class= serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
