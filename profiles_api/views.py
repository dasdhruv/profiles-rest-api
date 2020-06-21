from rest_framework.views import APIView
from rest_framework.response import Response

class HelloApiView(APIView):
    def get(this, request, format = None):
        an_apiViews = ['Uses HTTP methods as function (get, put, post, delete, patch)','is similar to a traditional django view',
        'Gives you most control over your app logic','is mapped manually to your URLs']

        return Response({'message':"Hello World", 'an_apiViews':an_apiViews})
