def who_is_paying(name):
    return [name] if len(name) < 3 else [name, name[:2]]
