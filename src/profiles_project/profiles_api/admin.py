from django.contrib import admin	# => This will import the admin module which needed to resiter our custom user profile
from . import models			# => This will import the model from the same apps directory

# Register your models here.

admin.site.register(models.UserProfile)	 # => This will register the 'UserProfile' to the django admin using the 'admin.site.register' module
