def individual_user(user) -> dict:
    return {
        "id": str(user["_id"]),
        "name": user["name"],
        "email": user["email"],
        "hashed_password": user["hashed_password"],
        "created_at": user["created_at"]
    }

def user_lists(users) -> list:
    return [individual_user(user) for user in users]