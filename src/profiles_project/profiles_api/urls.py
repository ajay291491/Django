from django.conf.urls import url	                # This module is to handle the url
from django.conf.urls import include                # Using for including the router.urls for ViewSet
from rest_framework.routers import DefaultRouter    # Importing the DefaultRouter class to handle urls for ViewSet

from . import views			        # We are importing views.py in our apps base directory here

router = DefaultRouter()
router.register('hello-viewset', views.HellowViewSet, base_name='hello-viewset')

urlpatterns = [ 
    
    # Using the url module, we are defining the api view 'hello-view/'
    # hello-view will display the get method defined under the HelloApiView class under the 'views.py' as the view
    url(r'^hello-view/', views.HelloApiView.as_view()),

    # Here we are making the advntage of include module and DefaultRouter class
    # Using this urls will automatically mapped according to how they are associated to objects
    url(r'', include(router.urls))
    ]


