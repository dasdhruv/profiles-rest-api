from django.urls import path
from profiles_api import views

urlpatterns = [
    # as_view is the standard function that we call to convert our api view's class HelloApiView rended by the URLs
    # So, in our case it will call the function get if a HTTP get is requested
    path('hello-view/', views.HelloApiView.as_view())
]
