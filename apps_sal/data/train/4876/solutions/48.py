def hello(name=0):
    if name:
        name = name.title()
        return f'Hello, {name}!'
    else:
        return f'Hello, World!'
