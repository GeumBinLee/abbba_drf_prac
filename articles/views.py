from rest_framework.views import APIView
from rest_framework.response import Response
from articles.models import Article, Comment
from rest_framework import status
from django.shortcuts import get_object_or_404
from articles.serializers import ArticleListSerializer, ArticleCreateSerializer, CommentCreateSerializer,ArticleDetailSerializer, CommentSerializer
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly 


class ArticleListView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request) :
        articles = Article.objects.all()
        serializer = ArticleListSerializer(articles, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request) :
        serializer = ArticleCreateSerializer(data=request.data)
        if serializer.is_valid() :
            serializer.save(author=request.user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else :
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ArticleDetailView(APIView) :
    permission_classes = [IsAuthenticatedOrReadOnly ]
    
    def get(self, request, article_id) :
        article = get_object_or_404(Article, id=article_id)
        serializer = ArticleDetailSerializer(article)
        return Response(serializer.data)
    
    def put(self, request, article_id) :
        article = get_object_or_404(Article, id=article_id)
        serializer = ArticleCreateSerializer(article, data=request.data)
        if request.user == article.author :
            if serializer.is_valid() :
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response("수정 놉")
    
    def delete(self, request, article_id) :
        article = get_object_or_404(Article, id=article_id)
        if request.user == article.author :
            article.delete()
            return Response("삭제!")
        return Response("삭제 놉")

class CommentView(APIView) :
    permission_classes = [IsAuthenticated]
    
    def get(self, request, article_id) :
        article = get_object_or_404(Article, id=article_id)
        comments = article.comment.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, article_id) :
        serializer = CommentCreateSerializer(data=request.data)
        if serializer.is_valid() :
            serializer.save(author=request.user, post=get_object_or_404(Article, id=article_id))
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CommentDetailView (APIView) :
    permission_classes = [IsAuthenticatedOrReadOnly ]
    
    def put(self, request, article_id, comment_id) :
        comment = get_object_or_404(Comment, id=comment_id)
        if request.user == comment.author :
            serializer = CommentCreateSerializer(comment, data=request.data)
            if serializer.is_valid() :
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response("수정 놉")
    
    def delete(self, request, article_id, comment_id) :
        comment = get_object_or_404(Comment, id=comment_id)
        if request.user == comment.author :
            comment.delete()
            return Response("삭제!")
        return Response("삭제 놉")


class LikeView(APIView) :
    permission_classes = [IsAuthenticated]
    
    def post(self, request, article_id):
        article = get_object_or_404(Article, id=article_id)
        if request.user in article.likes.all():
            article.likes.remove(request.user)
            return Response("💔💔💔💔", status=status.HTTP_200_OK)
        else:
            article.likes.add(request.user)
            return Response("💖💖💖💖", status=status.HTTP_200_OK)

