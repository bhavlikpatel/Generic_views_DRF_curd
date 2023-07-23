'''from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.views import APIView
from rest_framework import status
from django.http import Http404'''
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from .generic import UserRetriveUpdateDelete

from .models import User
from .serializers import UserSerializer


class UserRetrieveUpdateDestroyAPI(UserRetriveUpdateDelete):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserListCreateAPIView(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer    


'''Using old and long way
class UserApiList(APIView):

    def get_user (request, pk):
        try:
            if pk is not None:
                return User.objects.get(id=pk)
            return User.objects.all()
        except User.DoesNotExist:
            raise Http404

    def get(self, request, pk=None, format=None):
        serializer = UserSerializer(self.get_user(pk), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request,pk=None,format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            serializer = UserSerializer(self.get_user(pk), many=True)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)


class UserApiDetail(APIView):

    def get(self, request, pk, format=None):
        user_list = UserApiList()
        serializer = UserSerializer(user_list.get_user(pk))
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request,pk,format=None):
        user_list = UserApiList()
        serializer = UserSerializer(user_list.get_user(pk), data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)'''