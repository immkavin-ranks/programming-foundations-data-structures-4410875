user_preferences = {
    "timezone": "GMT",
    "language": "English",
    "notifications": None,
    "currency": "USD",
    "theme": None
}

# improved version of 03_04b/main.py
def update_preferences(user_pref):
    return {key: value for key, value in user_pref.items() if value is not None}


print(update_preferences(user_preferences))
