from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from rest_framework import status
from .serializers import CommentSerializer
# Create your views here.
@api_view(['GET', 'POST'])
def comment_list(request):
    if request.method == "GET":
        all_commenst = Comments.objects.all()
        serializer = CommentSerializer(all_commenst, many=True)
        return Response({'status':200, 'all_data': serializer.data})


    if request.method == "POST":
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT', 'DELETE'])
def edit_delete(request, pk):
    try:
        get_data = Comments.objects.get(id=pk)
    except Comments.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == "PUT":
        serializer = CommentSerializer(get_data, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 200, 'all_data': serializer.data})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        get_data.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

