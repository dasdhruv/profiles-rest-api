## Call this program http://127.0.0.1:8000/api/hello-view/
from rest_framework.views import APIView
from rest_framework.response import Response
# status module will contain the list of handy HTTP status codes that you can use when you return responds from API
from rest_framework import status
from profiles_api import serializers

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
