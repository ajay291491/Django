from django.shortcuts import render

from rest_framework.views import APIView		# This imports the APIView class from the django rest_framework views 
from rest_framework.response import Response		# This will process output which we need to return in JSON format with status codes 

# Create your views here.

class HelloApiView(APIView):
    """ Test API View """
    
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


        # response has to be always send it a dictionary format, for that we will associate our list with a key as seen below 
        return Response({'Message' : 'Hello, welcome to Ajay\'s first api endpoint', 'an_apiview': an_apiview, 'family_details' : family_details })

