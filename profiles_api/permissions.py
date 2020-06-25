from rest_framework import permissions

class UpdateOwnProfile(permissions.BasePermission):
    """ Authenticate users to update profile  """

    # has_object_permission class is django class. So, keep the name as it is and do not change it
    def has_object_permission(this, request, view, obj):
        """ a user should see his/her profile and others profile but should not be able to perform the update on others profile """
        """ But the user can update his/her own profile """

        """ If the method being used is HTTP get then it will be in safe method """
        if request.method in permissions.SAFE_METHODS:
            return True

        """ If the method is being used is not in safe method """
        """ Django assign authenticated user to request.user.id """
        if (obj.id == request.user.id):
            return True

class UpdateOwnStatus(permissions.BasePermission):
    """ Authenticate users to update profile  """

    # has_object_permission class is django class. So, keep the name as it is and do not change it
    def has_object_permission(this, request, view, obj):
        """ a user should see his/her profile and others profile but should not be able to perform the update on others profile """
        """ But the user can update his/her own profile """

        """ If the method being used is HTTP get then it will be in safe method """
        if request.method in permissions.SAFE_METHODS:
            return True

        """ If the method is being used is not in safe method """
        """ Django assign authenticated user to request.user.id """
        if (obj.user_profile.id == request.user.id):
            return True
