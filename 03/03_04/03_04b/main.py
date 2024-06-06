user_preferences = {
    "timezone": "GMT",
    "language": "English",
    "notifications": None,
    "currency": "USD",
    "theme": None
}

# O(n)
def update_preferences(user_pref):
    update_pref = {}
    for key, value in user_pref.items():
        if value is not None:
            update_pref[key] = value
    return update_pref


print(update_preferences(user_preferences))
