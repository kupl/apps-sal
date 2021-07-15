def hello(name = None):
    """ This function returns 'Hello, {Name}!' to a given name or says 'Hello, World!' if name is not given. """
    if name is None or len(name) == 0:
        return 'Hello, World!'
    name = name.capitalize()
    return f'Hello, {name}!'
