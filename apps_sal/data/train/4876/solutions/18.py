def hello(*name):
    if len(name) > 0:
        return 'Hello, ' + name[0].lower().capitalize() + '!' if len(name[0]) > 0 else 'Hello, World!'
    return 'Hello, World!'
