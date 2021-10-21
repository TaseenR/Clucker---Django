from django.core.validators import RegexValidator
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    username = models.CharField(
        max_length=30,
        unique=True,
        validators=[RegexValidator(
            regex=r'@\w{3,}$',
            message= 'Username must consist of @ followed by atleast three alphanumericals'
        )])
    first_name =  models.CharField(max_length=50, blank= False)
    last_name = models.CharField(max_length=50, blank= False)
    email = models.EmailField(unique=True, blank=False)
    bio = models.CharField(max_length=520, blank=True)

class Post(models.Model):
    author = models.ForeignKey(User, on_delete= models.CASCADE)
    text = models.CharField(blank=False, max_length=200)
    created_at = models.DateTimeField(auto_now_add = True)
    
    class Meta:
        ordering = ['-created_at']
    