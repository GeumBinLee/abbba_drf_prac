from rest_framework.views import APIView
from rest_framework.response import Response
from users.models import User

from rest_framework import status
from django.shortcuts import get_object_or_404

from rest_framework.permissions import IsAuthenticated
from users.serializers import SignupSerializer, TokenObtainPairSerializer, ProfileSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

class SignupView(APIView):
    def post(self, request):
        serializer = SignupSerializer(data = request.data)
        if serializer.is_valid() :
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = TokenObtainPairSerializer
    

class FollowView(APIView) :
    permission_classes = [IsAuthenticated]

    def post(self, request, id):
        user = get_object_or_404(User, id=id)
        if request.user in user.followers.all() :
            user.followers.remove(request.user)
            return Response("Follow", status=status.HTTP_200_OK)
        else :
            user.followers.add(request.user)
            return Response("Unfollow", status=status.HTTP_200_OK)


class ProfileView(APIView) :
    permission_classes = [IsAuthenticated]

    def get(self, request, id) :
        user = get_object_or_404(User, id=id)
        serializer = ProfileSerializer(user)
        return Response(serializer.data)