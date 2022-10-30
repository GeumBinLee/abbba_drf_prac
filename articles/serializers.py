from rest_framework import serializers
from articles.models import Article, Comment
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class ArticleListSerializer(serializers.ModelSerializer):
    author = serializers.SerializerMethodField()
    like_count = serializers.IntegerField(source = 'likes.count', read_only=True)
    comment_count = serializers.IntegerField(source ='comment.count', read_only=True)
    
    def get_author(self, obj):
        return obj.author.email
    
    class Meta:
        model = Article
        fields = '__all__'


class ArticleCreateSerializer(serializers.ModelSerializer) :
    class Meta : 
        model = Article
        fields =  ("title", "content")


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SerializerMethodField()
    
    def get_author(self, obj):
        return obj.author.email
    
    class Meta:
        model = Comment
        fields = '__all__'

class CommentCreateSerializer(serializers.ModelSerializer) :
    class Meta : 
        model = Comment
        fields =  ("content",)
        
class ArticleDetailSerializer(serializers.ModelSerializer):
    comment = CommentSerializer(many=True)
    author = serializers.SerializerMethodField()
    likes = serializers.StringRelatedField(many=True)
    
    def get_author(self, obj):
        return obj.author.email
    class Meta:
        model = Article
        fields = '__all__'
        
