import datetime


def greeting(user_name: str):
    currentTime = datetime.datetime.now()
    currentTime.hour

    if currentTime.hour < 12:
        greeting_text = "Good Morning"
    elif 12 <= currentTime.hour < 18:
        greeting_text = "Good Afternoon"
    else:
        greeting_text = "Good Evening"

    return f"{greeting_text}, {user_name}"
