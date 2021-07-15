def who_is_paying(name):
    return len(name) > 2 and [name, name[:2]] or [name]
