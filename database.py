def get_user(username):
    # BUG 3: SQL Injection
    query = f"SELECT * FROM users WHERE username = '{username}'"
    return query