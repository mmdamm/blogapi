from rest_framework.permissions import BasePermission

SAFE_METHODS = ('GET', 'HEAD', 'OPTIONS')


class IsOwnerOrSuperUser(BasePermission):
    def has_object_permission(self, request, view, obj):
        print(request.method)
        return bool(
            request.user.is_superuser or
            request.user.is_authenticated and obj.author == request.user
        )


class IsAuthor(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method == "POST":
            print('======================')
            print(request.user.id)
            print('======================')
            obj.author.id = request.user.id
            return True


class IsSuperUser(BasePermission):
    def has_permission(self, request, view):
        if request.method=="POST":
            if request.user and not request.user.is_authenticated:
                print("============================================")
                return True
        # return bool(
        #     request.user.is_authenticated and request.user.is_superuser
        #
        # )
