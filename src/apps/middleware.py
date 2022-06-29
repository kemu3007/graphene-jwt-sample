from collections.abc import Callable

from django.core.exceptions import PermissionDenied
from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse
from rest_framework_simplejwt.authentication import JWTAuthentication

exampt_urls = ["api/token", "admin"]


class AuthMiddleware:
    def __init__(self, get_response: Callable[[WSGIRequest], HttpResponse]):
        self.get_response = get_response

    def __call__(self, request: WSGIRequest):
        if any([url in request.path for url in exampt_urls]) or (
            request.user.is_authenticated or JWTAuthentication().authenticate(request)
        ):
            return self.get_response(request)
        raise PermissionDenied
