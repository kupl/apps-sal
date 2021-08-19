def hello(name: str = '') -> str:
    """ Get "Hello, ${name}!" to a given name, or says "Hello, World!" if name is not given. """
    return f"Hello, {name.title() or 'World'}!"
