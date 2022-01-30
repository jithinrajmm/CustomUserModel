

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin,BaseUserManager

from django.utils.translation import gettext_lazy as _ 

#  this gettext_lazy is used to translate the languages from one region to other while access instead of calling the feild 

# This is and manager for the Custom user model 
#  if we are using the default feild in  the user models then we need to define the UserManager
#  the use of this BaseUserManager is we are defining the create_user method and create_superuser method with the newly added feilds 
#  in the user custom models 
#  and what is the manager
#  in django the manager is the interface through which database query operation provided to the django model
''' the manager is the interface between model and database query operations '''

class CustomUserManager(BaseUserManager):

    # just creating the superuser method and its return the createuser method

    def create_superuser(self,email,first_name,user_name,password,**other_fields):

        other_fields.setdefault('is_staff',True)
        other_fields.setdefault('is_superuser',True)
        other_fields.setdefault('is_active',True)
    #  this is and validation checkup while creation method
        if other_fields.get('is_staff') is not True:
            raise ValueError('Super user is_staff must be True')
        if other_fields.get('is_superuser') is not True:
            raise ValueError('is_superuser must set to True')
        if other_fields.get('is_active') is not True:
            raise ValueError('is_active must be set to True')


        #  returning to the create_user method that method will create the superuser with otherfields values

        return self.create_user(email,first_name,user_name,password,**other_fields)

    def create_user(self,email,first_name,user_name,password,**other_fields):

        if not email:
            raise ValueError(_('the email is madatory'))

        email = self.normalize_email(email)
        user = self.model(email=email,first_name=first_name,user_name=user_name,**other_fields)
        user.set_password(password)
        user.save()
        return user



# Create your models here.




class CustomUser(AbstractBaseUser,PermissionsMixin):
    
    email = models.EmailField(_('enter the email'),unique=True,max_length=100)
    user_name = models.CharField(max_length=100,unique=True)
    first_name = models.CharField(max_length=100)
    start_date = models.DateTimeField(default=timezone.now)

    about = models.TextField(_('enter few words about you'),max_length=500)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['user_name','first_name']
    
    def __str__(self):
        return self.user_name
