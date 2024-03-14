# SIN DRF
'''from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
# Create your views here.
 
    
def home(request):
    
    return JsonResponse({'foo':'bar'})'''

#CON DRF    
from rest_framework import viewsets
from .models import Post, User
from .serializers import PostSerializer, UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    
    filterset_fields = ['title', 'user']
    search_fields = ['title', 'description']
    ordering_fields = ['title', 'created_at']
    ordering = ['-created_at']
    
 #   def get_serializer_class(self):
 #       pass
    
 #   def get_queryset(self):
 #       pass
 
 