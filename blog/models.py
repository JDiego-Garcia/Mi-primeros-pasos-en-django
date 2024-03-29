from django.db import models
from django.contrib.auth.models import User
# Create your models here.




class Post(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=100, null=True, blank=True,)
    description = models.TextField()
    
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
        
    def __str__(self):
        return self.title
    
    