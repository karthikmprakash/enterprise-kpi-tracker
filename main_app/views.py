from datetime import datetime

from django.shortcuts import render

from .utils.ui_helpers import greeting


# Create your views here.
def home(request):
    username = "Karthik"
    data = {
        "greeting": greeting(user_name=username),
        "username": username,
        "date": datetime.today().date(),
        "tasks": {"completed": 2, "requires_attention": 5, "pending": 10},
    }
    return render(request, "home.html", context=data)
