## Call this program http://127.0.0.1:8000/api/hello-view/
from rest_framework.views import APIView
from rest_framework.response import Response
# status module will contain the list of handy HTTP status codes that you can use when you return responds from API
from rest_framework import status
from profiles_api import serializers
from rest_framework import viewsets
# Importing to handle user profile creation and updating the same and to write queryset
from profiles_api import models
# TokenAuthentication is the type of authentication that we are going to use. It works by generating a random token string
# when the user loggs in and every request that we make to the API that we need to authenticate we add this token to the
# request. And thats effectively a password to check the evry request made is authenticating correctly.
from rest_framework.authentication import TokenAuthentication
from profiles_api import permissions
# To add the search functionality
from rest_framework import filters
# To generate token each time user loggs in to our system
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.permissions import IsAuthenticatedOrReadOnly
#from rest_framework.permissions import IsAuthenticated


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


class UserProfileViewSet(viewsets.ModelViewSet):

	""" Handle creating and updating profile """
	serializer_class = serializers.UserProfileSerializer
	# The Django rest_framework knows the standard functions that you wanna perform on a model viewset
	queryset = models.UserProfile.objects.all()

	# Lets authenticate the user
	# Remember to add a comma below so that authentication_class gets created as a tuple
	# instead of just a single item
	authentication_classes = (TokenAuthentication,)
	permission_classes = (permissions.UpdateOwnProfile,)

	# Let us add a search filter so that user can search a profile by their name or email
	# Make sure that you should not change the variable names
	filter_backends = (filters.SearchFilter,)
	search_fields = ('name','email')



#http://127.0.0.1:8000/api/Login/
class UserLoginApiView(ObtainAuthToken):
	"""Handle creating user authentication tokens"""
	renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES





class ProfileFeedModelsViewSet(viewsets.ModelViewSet):

	serializer_class = serializers.ProfileFeedModelsSerializer
	# The Django rest_framework knows the standard functions that you wanna perform on a model viewset
	queryset = models.ProfileFeedModels.objects.all()

	permission_classes = (permissions.UpdateOwnStatus, IsAuthenticatedOrReadOnly)
	#permission_classes = (permissions.UpdateOwnStatus, IsAuthenticated)

	# The perform_create functions is a handy functions provided by django rest_framework
	# it allows you to override the behaviour or customize the behaviour.
	# It allows you to create objects through a model viewsets
	# this is called everytime when we request HTTP post
	def perform_create(this, serializer):
		serializer.save(user_profile=this.request.user)
