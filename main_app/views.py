from datetime import datetime
from urllib.parse import quote_plus, urlencode

from django.conf import settings
from django.shortcuts import redirect, render
from django.urls import reverse

from .utils.ui_helpers import greeting


def check_authentication(request):

    if request.user.is_authenticated:
        return True
    else:
        return False


def logout(request):
    request.session.clear()

    return redirect(
        f"https://{settings.SOCIAL_AUTH_AUTH0_DOMAIN}/v2/logout?"
        + urlencode(
            {
                "returnTo": request.build_absolute_uri(reverse("home")),
                "client_id": settings.SOCIAL_AUTH_AUTH0_KEY,
            },
            quote_via=quote_plus,
        ),
    )


# Create your views here.
def home(request):
    if check_authentication(request):
        user = request.user
        auth0_user = user.social_auth.get(provider="auth0")
        user_data = {
            "user_id": auth0_user.uid,
            "name": user.first_name,
            "picture": auth0_user.extra_data["picture"],
        }
        data = {
            "greeting": greeting(user_name=user.first_name),
            "username": user.first_name,
            "email": user.email,
            "date": datetime.today().date(),
            "tasks": {"completed": 2, "requires_attention": 5, "pending": 10},
            "user_data": user_data,
        }
        return render(request, "home.html", context=data)
    else:
        return redirect("/login/auth0")
