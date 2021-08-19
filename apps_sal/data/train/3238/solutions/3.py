def get_users_ids(string):
    return [uid.replace("uid", "", 1).strip() for uid in string.replace("#", "").lower().split(", ")]
