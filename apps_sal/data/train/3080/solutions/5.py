def who_is_paying(name):
    return [name] * (len(name) > 2) + [name[:2]]
