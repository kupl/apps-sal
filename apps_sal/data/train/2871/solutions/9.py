def starts_with(st, prefix):
    if not len(prefix) <= len(st):
        return False
    else:
        return st[:len(prefix)] == prefix
