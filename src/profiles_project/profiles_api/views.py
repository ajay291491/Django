from django.shortcuts import render

from rest_framework.views import APIView		# This imports the APIView class from the django rest_framework views 
from rest_framework.response import Response	# This will process output which we need to return in JSON format with status codes
from rest_framework import status			    # This will help to return a status code for for API

from rest_framework import viewsets              # This module will take care of the Viewset operations

from . import serializers

# Create your views here.

class HelloApiView(APIView):
    """ Test API View """

    serializer_class = serializers.HelloSerializer
    
    def get(self, request, format=None):
        """ Returns a list of APIView Features """

        an_apiview = [
            'Uses HTTP methods as functions (get, post, patch, put , delete)',
            'It is similar to traditional Django view',
            'Gives you the most control over your application logic', 
            'Its manually mapped to URLs'
        ]

        family_details = {
            'Father'   : 'Ajayaghosh V L',
            'Mother'   : 'Aparna A',
            'Daughter' : 'Vaiga Shanti A',
            'Son'      : 'Rishi Krishna A',
        }

        fstab_file = open('/etc/fstab', 'r')
        content = fstab_file.readlines()


        # response has to be always send it a dictionary format, for that we will associate our list with a key as seen below 
        #return Response({'Message' : 'Hello, welcome to Ajay\'s first api endpoint', 'an_apiview': an_apiview, 'family_details' : family_details , 'fstab' : content})
        return Response({'fstab contents' : content})

    def post(self, request):
        """ This will return the same name which is getting pasted """

        """ Meaning of below is this will initialize the 'serializer' with HelloSerializer which we defined in the serializers.py in apps base dir
            Also the 'request' will contain all information while we make a post request, amongst that actual data can be fetched out using 'request.data' """
        serializer = serializers.HelloSerializer(data=request.data)

        if serializer.is_valid():
            name = serializer.data.get('name') # With this 'name' variable which declared within 'HelloSerializer' will assigned to name variable here 
            message = 'Hello {0}'.format(name) # Formatting technique in python 
            return Response({'message': message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) # This will retun error and HTTP status code using Response module

    def put(self, request, pk=None):
        """ This method will help to update an object """

        return Response({"message" : "You have used the put method"})

    def patch(self, request, pk=None):
        """ This method will help to update few fields in the object """

        return Response({"message": "You have used the patch method"})

    def delete(self, request, pk=None):
        """ This methhod will help to delete an object """

        return Response({"message" : "This method will delete an object"})

        

class HellowViewSet(viewsets.ViewSet):
    """Test Hello Viewset"""

    def list (self, request):
        """Return a Hello Message"""
        a_viewset = [
            "Uses actions (list, create, retrieve, update, partial_update",
            "Automatically maps URLs using routers",
            "Provide more functionality with less code",
        ]

        return Response({'message' : 'This is a viewset', 'a_viewset': a_viewset})
