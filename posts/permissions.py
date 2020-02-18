from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):

    # переопределим фукнцию has_object_permission базового класса BasePermission
    def has_object_permission(self, request, view, obj):

        # мы хотим разрешить только чтение для всех запросов
        if request.method in permissions.SAFE_METHODS: # GET, OPTIONS и HEAD
            return True

        # для запросов на запись, таких как редактирование или удаление,
        # автор должен быть тот же, что и текущий вошедший в систему пользователь.
        return obj.author == request.user
