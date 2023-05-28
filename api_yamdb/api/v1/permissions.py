from rest_framework import permissions


class IsAdmin(permissions.BasePermission):
    message = 'Only Admins allowed'

    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.is_admin


class IsAdminOrReadOnly(permissions.BasePermission):
    message = 'Only Admins allowed'

    def has_permission(self, request, view):
        return (request.method in permissions.SAFE_METHODS
                or (request.user.is_authenticated and request.user.is_admin))


class IsAdminModeratorAuthorOrReadOnly(permissions.IsAuthenticatedOrReadOnly):
    message = 'Only Admins, Moderators or Author allowed'

    def has_object_permission(self, request, view, obj):
        return (request.method in permissions.SAFE_METHODS
                or request.user.is_admin or request.user.is_moderator
                or obj.author == request.user)
