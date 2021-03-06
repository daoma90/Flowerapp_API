from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import CommentSerializer
from .models import Comment

# Create your views here.

@api_view(['GET'])
def apiOverview(request):

    api_urls = {
        'List':'/comment-list/<str:pk>/', 
        'Create':'/comment-create', 
        'Update':'/comment-update/<str:pk>/', 
        'Delete':'/comment-delete/<str:pk>/'
        }

    return Response(api_urls)

@api_view(['GET'])    
def commentList(request, pk):
    comments = Comment.objects.filter(flowerId=pk).order_by('-timeStamp')
    serializer = CommentSerializer(comments, many=True)
    return Response(serializer.data)

@api_view(['POST'])    
def commentCreate(request):
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])    
def commentUpdate(request, pk):
    comment = Comment.objects.get(id=pk)
    serializer = CommentSerializer(instance=comment, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])    
def commentDelete(request, pk):
    comment = Comment.objects.get(id=pk)
    comment.delete()
    return Response('Item deleted')