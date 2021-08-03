def who_is_paying(name=''):
    return [name, name[:2]] if name != name[:2] else [name]
