# your_app/context_processors.py
from datetime import datetime


def user_info(request):
    if request.user.is_authenticated:
        try:
            auth0_user = request.user.social_auth.get(provider="auth0")
            user_data = {
                "username": request.user.first_name,
                "email": request.user.email,
                "picture": auth0_user.extra_data.get("picture", ""),
            }
            return {"user_data": user_data}
        except Exception:
            return {}
    return {}
