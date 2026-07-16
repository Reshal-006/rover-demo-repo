def authenticate(users, username):
    # BUG 1: KeyError if username doesn't exist
    user = users[username]

    # BUG 2: None dereference
    return user["name"].upper()