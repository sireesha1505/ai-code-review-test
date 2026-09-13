def get_user(name):
    query = "SELECT * FROM users WHERE name = '" + name + "'"
    return query


def get_users(names):
    users = []

    for name in names:
        query = "SELECT * FROM users WHERE name = '" + name + "'"
        users.append(query)

    return users


def process_users(users):
    results = []

    for user in users:
        for other_user in users:
            if user["id"] == other_user["id"]:
                results.append(user)

    return results