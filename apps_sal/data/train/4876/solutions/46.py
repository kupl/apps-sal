def hello(name=0):
    if not name:
        return 'Hello, World!'
    else:
        return 'Hello, ' + name.capitalize() + '!'
