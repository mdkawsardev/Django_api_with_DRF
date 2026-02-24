from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import CommentSerializer
# Create your views here.
@api_view(['GET'])
def comment_list(request):
    all_commenst = Comments.objects.all()
    serializer = CommentSerializer(all_commenst, many=True)
    return Response(serializer.data)
