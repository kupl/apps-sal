def hello(name=None):
    if name == '' or name == None:
        return f'Hello, World!'
    else:
        return f'Hello, {name.capitalize()}!'
