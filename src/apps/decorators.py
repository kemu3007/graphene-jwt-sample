import functools

from django.core.exceptions import PermissionDenied
from django.core.handlers.wsgi import WSGIRequest
from rest_framework_simplejwt.authentication import JWTAuthentication

exampt_urls = ["api/token", "admin"]


def jwt_decorator():
    def decorator(view_func):
        @functools.wraps(view_func)
        def _wrapped_view(request: WSGIRequest, *args, **kwargs):
            if JWTAuthentication().authenticate(request) or request.user.is_authenticated:
                return view_func(request, *args, **kwargs)
            raise PermissionDenied

        return _wrapped_view

    return decorator


def jwt_required(function):
    return jwt_decorator()(function)
