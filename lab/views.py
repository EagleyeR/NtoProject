import json
from lab.mqtt import client as mqtt_client
from django.http import JsonResponse
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *
import socket
class ProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        full_info = Profile.objects.get(pk=request.user.pk)
        return Response({"nick": request.user, "name": request.user.first_name,
                         "surname": request.user.last_name, "email": request.user.email,
                         "social": full_info.social, "labs": full_info.labs})

    def post(self, request):
        full_info = Profile.objects.get(pk=request.user.pk)
        user = User.objects.get(username=full_info.user)
        user.first_name = request.data["username"]
        user.email = request.data["email"]
        user.last_name = request.data["surname"]
        user.save()
        full_info.social = request.data.social
        full_info.save()
        return Response(1)


class AdminView(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request):
        pass

    def post(self, request):
        pass


class UserView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        pass

    def post(self, request):
        pass


def publish_message(request):
    request_data = json.loads(request.body)
    rc, mid = mqtt_client.publish(request_data['topic'], request_data['msg'])
    return JsonResponse({'code': rc})


