from django.db import models
from django.contrib.auth.models import AbstractUser,PermissionsMixin
from .manager import UserManager
from django.utils.translation import gettext_lazy as _
from rest_framework_simplejwt.tokens import RefreshToken
# User Registeration  Model.
class User(AbstractUser,PermissionsMixin):
    first_name = models.CharField(max_length=100, verbose_name = _("firstname"))
    last_name = models.CharField(max_length=100, verbose_name = _("lastname"))
    email = models.EmailField(unique=True,verbose_name = _("email"))
    password = models.CharField(max_length=100,verbose_name = _("password"))
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    last_login = models.DateTimeField(auto_now_add=True)
    date_joined = models.DateTimeField(auto_now=True)
    username = None
    objects = UserManager()

    
    USERNAME_FIELD = 'email'
    
    REQUIRED_FIELDS = ["first_name","last_name"]
    
       
    def __str__(self):
        return  self.first_name + " " +  self.last_name
    
    @property
    def get_full_name(self):
        return f"{self.first_name}{self.last_name}"
    
    def token(self):
       refresh = RefreshToken.for_user(self)
       return {
           'refresh': str(refresh),
           'access': str(refresh.access_token)
       }

