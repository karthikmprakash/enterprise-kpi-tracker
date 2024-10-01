from datetime import datetime

from django.shortcuts import render, redirect

from .utils.ui_helpers import greeting


# def check_authentication(request):

#     if request.user.is_authenticated:
#         return redirect("/home")
#     else:
#         return redirect("/login/auth0")


def check_authentication(request):

    if request.user.is_authenticated:
        return True
    else:
        return False


# Create your views here.
def home(request):
    user = request.user

    # auth0_user=user.social_auth.get(provider='auth0')

    # user_data={
    #     'user_id':auth0_user.uid,
    #     'name':user.first_name,
    #     'picture':auth0_user.extra_data['picture']
    # }

    # context={
    #     'user_data':json.dumps(user_data,indent=4),
    #     'auth0_user':auth0_user
    # }

    # username = "Karthik"

    if check_authentication(request):
        data = {
            "greeting": greeting(user_name=user.first_name),
            "username": user.first_name,
            "date": datetime.today().date(),
            "tasks": {"completed": 2, "requires_attention": 5, "pending": 10},
        }
        return render(request, "home.html", context=data)
    else:
        return redirect("/login/auth0")
