from django.conf.urls import url	# This module is to handle the url
from . import views			# We are importing views.py in our apps base directory here 

urlpatterns = [ 
    
    # Using the url module, we are defining the api view 'hello-view/'
    # hello-view will display the get method defined under the HelloApiView class under the 'views.py' as the view
    url(r'^hello-view/', views.HelloApiView.as_view()),	
    ]
