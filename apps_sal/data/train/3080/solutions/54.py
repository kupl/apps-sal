def who_is_paying(name):
    # your code
    return [name, name[:2]] if len(name) > 2 else [name[:2]]
