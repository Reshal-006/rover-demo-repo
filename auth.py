def authenticate(users, username):
    if not isinstance(users, dict) or username not in users:
        return None
    
    user = users[username]
    if not isinstance(user, dict) or "name" not in user or user["name"] is None:
        return None

    return user["name"].upper()