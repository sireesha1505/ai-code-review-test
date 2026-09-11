def multiply(a, b):
    return a * b


def get_user_query(user_input):
    query = "SELECT * FROM users WHERE name = '" + user_input + "'"
    return query