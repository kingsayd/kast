from django.db import models

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class UserManager(BaseUserManager):

    def create_user(self,first_name,last_name,username, email, password=None, ):
        """Creates and saves a new user"""
        if not email:
            raise ValueError('لا بد من ادخال ايميل صحيح')
        if not username:
            raise ValueError('need correct username')
        user = self.model(email=self.normalize_email(email), username = username ,first_name = first_name ,last_name = last_name ,)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self,first_name,last_name, email,username, password):
        user = self.create_user(email=self.normalize_email(email), username = username, first_name = first_name ,last_name = last_name, password = password,)
        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class Account(AbstractBaseUser):
    """Custom user model that uses email instead of username"""

    first_name    = models.CharField(max_length=50,default="",editable=False)
    last_name     = models.CharField(max_length=50,default="",editable=False)
    username      = models.CharField(max_length=50,unique=True,default="",editable=False)
    email        = models.EmailField(max_length=100, unique=True)
    phone_number = models.CharField(max_length=50)


    date_joind    = models.DateTimeField(auto_now_add=True)
    last_login    = models.DateTimeField(auto_now_add=True)
    is_admin      = models.BooleanField(default=False)
    is_staff      = models.BooleanField(default=False)
    is_active     = models.BooleanField(default=False)
    is_superadmin    = models.BooleanField(default=False)



    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS =['username','first_name','last_name']

    objects = UserManager()

    def __str__(self):
        return self.email

    def has_perm(self,perm ,obj=None):
        return self.is_admin

    def has_module_perms(self,add_label):
        return True







# Create your models here.
