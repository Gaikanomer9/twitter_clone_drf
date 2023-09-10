from rest_framework.permissions import SAFE_METHODS, BasePermission


class IsAuthorOrReadOnly(BasePermission):
    message = 'Изменять {} может только автор!'

    def has_object_permission(self, request, view, obj):
        self.message = self.message.format(type(obj).__name__)
        return (request.method in SAFE_METHODS
                or obj.author == request.user)