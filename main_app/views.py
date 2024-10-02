from datetime import datetime
from urllib.parse import quote_plus, urlencode

from django.conf import settings
from django.shortcuts import redirect, render
from django.urls import reverse

from .utils.ui_helpers import greeting


def login(request):
    return redirect(request.build_absolute_uri(reverse("callback")))


def callback(request):
    return redirect(request.build_absolute_uri(reverse("home")))


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
    user = request.user
    data = {
        "greeting": greeting(user_name=user.first_name),
        "date": datetime.today().date(),
        "tasks": {"completed": 2, "requires_attention": 5, "pending": 10},
    }
    return render(request, "home.html", context=data)


def dashboard(request):
    return render(request=request, template_name="dashboard.html")
