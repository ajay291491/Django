from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager

# Create your models here.

class UserProfileManager(BaseUserManager):
    """ Helps Django to work with the custom user profile which we created """

    def createuser(self, email, name, password=None):
        """ Helps to create a new user profile objects """
        
        if not email:
            raise ValueError('User must have an email address')
        #elif not name:
        #    raise ValueError('User must have a name specified')

        # This will normalize the email by setting everything to lowercase 
        email = self.normalize_email(email)

        # This will create a normal user with the provided information
        user  = self.model(email=email, name=name)
        
        # This will set the password and store it in database as a hash
        user.set_password(password)

        # This will save the user details in the database 
        user.save(using=self.db)

        return user

    def create_superuser(self, email, name, password): 
       """ Creates a super user with the given details """

       # Using the same 'createuser' function defined within the class to create the user
       user = self.createuser(email, name, password)
 
       # Set the user as a Super user and add to group staff
       user.is_superuser = True
       user.is_staff     = True 
       
       # Save the user and retun the user details 
       user.save(using=self._db)
       return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """ Represents 'user profile' inside our system and inherited form AbstractBaseUser and PermissionsMixin """

    email     = models.EmailField(max_length=255, unique=True) 
    name      = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff  = models.BooleanField(default=False)

   
    # Object manager (This will be covered in next lesson)
    objects = UserProfileManager()
   
    # Standard djano fileds for user profle 
    USERNAME_FIELD  = 'email'
    REQUIRED_FIELDS = ['name']
    
    def get_full_name(self):
        """ Used to get a user full name """

        return self.name

    def get_short_name(self):
        """ Used to get the short name """

        return self.name 

    def __str__(self):
        """ Django uses this function when it needs to convert the object to a string this is manadatory """

        return self.email
     
