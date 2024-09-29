from datetime import datetime

from django.shortcuts import render


# Create your views here.
def home(request):
    data = {
        "username": "Karthik",
        "date": datetime.today(),
        "tasks": {"completed": 2, "requires_attention": 5, "pending": 10},
    }
    return render(request, "home.html", context=data)
