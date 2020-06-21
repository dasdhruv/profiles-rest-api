## Call this program http://127.0.0.1:8000/api/hello-view/
from rest_framework.views import APIView
from rest_framework.response import Response
# status module will contain the list of handy HTTP status codes that you can use when you return responds from API
from rest_framework import status
from profiles_api import serializers
from rest_framework import viewsets

class HelloApiView(APIView):
    # The serializer_class function comes with the class APIView that retrieves the configured serializes class for our view
    serializer_class = serializers.HelloSerializer
    def get(this, request, format = None):
        an_apiViews = ['Uses HTTP methods as function (get, put, post, delete, patch)','is similar to a traditional django view',
        'Gives you most control over your app logic','is mapped manually to your URLs']
        return Response({'message':"Hello World", 'an_apiViews':an_apiViews})

    def post(this, request):
        # The serializer_class function comes with the class APIView that retrieves the configured serializes class for our view
        serializer = this.serializer_class(data = request.data)

        if serializer.is_valid():
            # The 'username' will be add a label to our web app
            name = serializer.validated_data.get('username')
            message = f'Hello {name}'
            return Response({'post_message':message})
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    def put(this, request, pk = None):
        return Response({'method':'PUT'})

    def patch(this, request, pk = None):
        return Response({'method':'PATCH'})

    def delete(this, request, pk = None):
        return Response({'method':'DELETE'})


# To call the class http://127.0.0.1:8000/api/Hello-ViewSet/
class HelloViewSets(viewsets.ViewSet):
    serializer_class = serializers.HelloSerializer
    def list(this, request):
        a_views_sets = ['Uses actions (list, create, retrieve, update, update partial)','Automatically maps to URLs using routers',
        'Provides more functionality using less code']
        return Response({'message':"Hello World", 'a_views_sets':a_views_sets})

    def create(this, request):
        # Create a new hello message
        serializer = this.serializer_class(data = request.data)

        if serializer.is_valid():
            # The 'username' will be add a label to our web app
            name = serializer.validated_data.get('username')
            message = f'Hello {name}'
            return Response({'post_message':message})
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    # To call the class http://127.0.0.1:8000/api/Hello-ViewSet/1
    # 1 is the primary key
    def retrieve(this, request, pk = None):
        return Response({'http_method':'GET'})

    def update(this, request, pk = None):
        return Response({'http_method':'PUT'})

    def partial_update(this, request, pk = None):
        return Response({'http_method':'PATCH'})

    def destroy(this, request, pk = None):
        return Response({'http_method':'DELETE'})
