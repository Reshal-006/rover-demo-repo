def authenticate(users, username):
    user = users.get(username)
    if user and isinstance(user, dict):
        name = user.get('name')
        if name:
            return name.upper()
    return None