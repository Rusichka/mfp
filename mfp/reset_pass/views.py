from __future__ import absolute_import, unicode_literals

from django.http import HttpResponseRedirect, Http404, HttpResponse
from django.contrib.auth.models import User

from rest_framework import status
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
#from .models import User
from .serializers import UserSerializer, ResetPasswordSerializer, NewPassCreateSerializer
#from django.core.mail import send_mail

class ResetPasswordView(generics.UpdateAPIView):
    permission_classes = (Not(IsAuthenticated),)
    serializer_class = ResetPasswordSerializer
    model = User
    
    def get(self, request, *args, **kwargs):
 
        username = request.query_params.get('username')
        user = User.objects.filter(username=username).first()
        if not user:
            return HttpResponse("User not found", status=404)
        #send_mail(
            #'Восстановление пароля',
            #'Пройдите по ссылке для восстановления пароля' + otc,
           # 'from@example.com',
          #  ['to@example.com'],
         #   fail_silently=False,
        #)
        return Response("Change password letter was sent to your e-mail.", status=status.HTTP_200_OK)
'''    
    def get_object(self, queryset=None):
        obj = self.request.user
        return obj

    def get(self, request, *args, **kwargs):
    
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            # Check user
            if not self.object.check_user(serializer.data.get("username")):
                return Response({"username": ["User is not found."]}, status=status.HTTP_400_BAD_REQUEST)
            return Response("Change password letter was sent to your e-mail.", status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
'''        

class NewPassCreateView(generics.UpdateAPIView):
    
    permission_classes = (Not(IsAuthenticated),)
    serializer_class = NewPassCreateSerializer
    model = User
    #permission_classes = (IsAuthenticated,)

    def get_object(self, queryset=None):
        obj = self.request.user
        return obj

    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            # Check old password
            if not self.object.check_password(serializer.data.get("old_password")):
                return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)
            # set_password also hashes the password that the user will get
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            return Response("Success.", status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
