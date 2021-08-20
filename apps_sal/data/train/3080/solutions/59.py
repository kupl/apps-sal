def who_is_paying(name):
    return [''] if name == '' else [name] if len(name) <= 2 else [name, name[0:2]]
