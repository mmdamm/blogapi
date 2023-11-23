from rest_framework.permissions import BasePermission

SAFE_METHODS = ('GET', 'HEAD', 'OPTIONS')


class IsOwnerOrSuperUser(BasePermission):
    def has_object_permission(self, request, view, obj):
        print(request.method)
        return bool(
            request.user.is_superuser or
            request.user.is_authenticated and obj.author == request.user
        )


