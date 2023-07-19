from typing import Any
from django import http
from django.shortcuts import render
from django.views import View


class Home(View):
    '''
    django.views.generic.base.View
    
    '''
    #accessible Http method via this view
    http_method_names = ['get', 'options']
    
    
    def setup(self, request, *args, **kwargs):
        '''
            initial setup for the view
        '''
        return super().setup(request, *args, **kwargs)
    
    
    def dispatch(self, request, *args, **kwargs):
        '''
        the middleman between request and response
        '''
        return super().dispatch(request, *args, **kwargs)
        

    def options(self, request, *args, **kwargs):
        '''
            showing the request headers.
            also you can override this, to modify headers.
        '''
        response = super().options(request, *args, **kwargs)
        response.headers['host'] = 'localhost'
        response.headers['user'] = request.user
        return response
    
    
    def http_method_not_allowed(self, request, *args, **kwargs):
        return render(request, 'method_not_allowed.html')

    
    def get(self, request):
        return render(request, 'home/home.html')
    