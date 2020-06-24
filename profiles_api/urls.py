from django.urls import path, include
from profiles_api import views
# Let us import a default routers for using viewsets
from rest_framework.routers import DefaultRouter

# To use viewsets
router = DefaultRouter()
router.register("Hello-ViewSet", views.HelloViewSets, base_name = "Hello-ViewSet")
# Let us register our create and update profile ViewSet
# unlike the Hello-ViewSet we dont need to specify the base_name as we have queryset in our UserProfileViewSets
router.register("profile", views.UserProfileViewSet)

urlpatterns = [
    # as_view is the standard function that we call to convert our api view's class HelloApiView rended by the URLs
    # So, in our case it will call the function get if a HTTP get is requested
    path('hello-view/', views.HelloApiView.as_view()),
    # We are going to add a path for a blank string
    # As you register new routes for the router object it generates a list of URLs which are associated for our viewsets
    path('', include(router.urls))
]
