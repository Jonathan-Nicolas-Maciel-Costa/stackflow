from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import BaseUserManager, AbstractUser

import jwt
from django.conf import settings
from datetime import datetime, timedelta

# Create your models here.

class UserManager(BaseUserManager):
    #REQUIRED_FIELDS = ['','username' , 'email' ,'', 'phone']

    def _create_user(self, username, email, birthday, password, **extra_fields):
        if not email:
            raise ValueError("O e-mail é obrigatório")
        if not username:
           raise ValueError("O username é obrigatório")
        
        email = self.normalize_email(email)
        """ username = seusername
         = seemail """
        
        user = self.model(username=username, email=email, birthday=birthday, **extra_fields)
        
        if password:
            user.set_password(password)
        user.save(using=self._db)
        return user
    
    def _create_super_user(self,  username, email, phone, password, **extra_fields):
        if not email:
            raise ValueError("O e-mail é obrigatório")
        if not username:
           raise ValueError("O username é obrigatório")
        if not phone:
            #raise ValueError("O phone é obrigatório")
            phone = None
        
        email = self.normalize_email(email)
        
        """ username = seusername
         = seemail """
        
        user = self.model( username=username, 
                           email=email, 
                           phone=phone, 
                           **extra_fields)
        
        if password:
            user.set_password(password)
        
        user.save(using=self._db)
        return user

    def create_user(self, username, email, birthday=None, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        extra_fields.setdefault('is_staff', True)

        print(password, '<<<')
        if not username:
            raise ValueError("O username é obrigatório")

        return self._create_user( username, email, birthday, password, **extra_fields)

    def create_superuser(self, username, email, phone, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser precisa ter is_superuser = True')
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser precisa ter is_staff = True')

        return self._create_super_user( username, email, phone, password, **extra_fields)



class CustomUser(AbstractUser):

    'image, username, email, phone, birthday'

    image = models.ImageField(upload_to='Media', blank=True, null=True, default='Media/no_image_dafaut.jpg')
    username = models.CharField(("Nome"), max_length=50, unique=False, primary_key=None)
    email = models.EmailField("E-mail", unique=True)
    phone = models.CharField("Telefone", max_length=15, blank=True, null=True)
    birthday = models.DateField('Data de Nascimento', blank=True, null=True)
    primeiro_login = models.DateField(("Quando a conta foi criada"), auto_now_add=True)
    
    
    is_staff = models.BooleanField('Membro da equipe', default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'phone']

    def __str__(self):
        return self.username

    objects = UserManager()
    
    @property
    def token(self):
        token = jwt.encode({'username': self.username, 'email': self.email, 
                            'exp': datetime.utcnow() + timedelta(hours=24)}, 
                           settings.SECRET_KEY, algorithm='HS256')
        return token