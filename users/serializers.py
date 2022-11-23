from rest_framework import serializers
from users.models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from articles.serializers import ArticleListSerializer
# 시리얼랄이저 예

class SignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            password=validated_data['password'],
            nickname=validated_data['nickname'],
            phone_number=validated_data['phone_number'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


class TokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        token['email'] = user.email
        token['nickname'] = user.nickname
        token['phone_number'] = user.phone_number

        return token


class ProfileSerializer(serializers.ModelSerializer):
    follow = serializers.StringRelatedField(many=True)  # 모델 이름
    followers = serializers.StringRelatedField(many=True)  # related_name 설정한 거

    article_set = ArticleListSerializer(many=True)
    
    likes = ArticleListSerializer(many=True)

    class Meta:
        model = User
        fields = '__all__'
