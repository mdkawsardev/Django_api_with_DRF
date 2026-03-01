from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from rest_framework import status
from .serializers import CommentSerializer
from rest_framework.views import APIView
# Create your views here.
# These operations are class based.
class Student_List(APIView):
    def get(self, request, format=None):
        all_data = Comments.objects.all()
        serializer = CommentSerializer(all_data, many=True)
        return Response({'status': 200, 'all_students': serializer.data})
    def post(self, request, format=None):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 200, 'msg': 'New data added successfully!', 'all_students': serializer.data})

class Edit_Students(APIView):
    def get_id(self, pk):
        try:
            return Comments.objects.get(id=pk)
        except Comments.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    def get(self, request, pk, format=None):
        get_data = self.get_id(pk)
        serializer = CommentSerializer(get_data)
        return Response(serializer.data)
    def put(self, request, pk, format=None):
        get_data = self.get_id(pk)
        serializer = CommentSerializer(get_data, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 200, 'msg': 'Data updated successfully!', 'all_students': serializer.data})
        return Response(status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk, format=None):
        get_data = self.get_id(pk)
        get_data.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)