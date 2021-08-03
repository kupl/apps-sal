from re import fullmatch


def validate_usr(username):
    return bool(fullmatch(r"[_0-9a-z]{4,16}", username))
