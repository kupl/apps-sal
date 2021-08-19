def hello(name='') -> str:
    """
    take (str: name) and return 'Hello, {name}!'
    if no name, return 'Hello, World!'
    """
    return f'Hello, {name.title()}!' if name else 'Hello, World!'
