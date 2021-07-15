def get_users_ids(string):
    return [w.replace("uid", "", 1).strip() for w in string.lower().replace("#", "").split(",")]
