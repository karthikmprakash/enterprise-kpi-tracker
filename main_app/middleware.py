from django.shortcuts import redirect
from django.urls import reverse


class AuthenticationMiddleware:
    """
    Middleware to ensure the user is authenticated for protected views.
    If the user is not authenticated, it redirects them to the login page.
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Paths that do not require authentication (like login and logout)
        allowed_paths = [
            "/complete/auth0",
            reverse("login"),
            reverse("logout"),
            reverse("callback"),
        ]

        # Check if user is authenticated, and request path is not in allowed paths
        if not request.user.is_authenticated and request.path not in allowed_paths:
            return redirect(reverse("login"))
        return self.get_response(request)
