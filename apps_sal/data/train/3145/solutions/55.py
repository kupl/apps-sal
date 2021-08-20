def greet(name: str) -> str:
    """
    takes a string name and returns a greeting
    """
    try:
        if type(name) is str:
            return f'Hello, {name} how are you doing today?'
    except TypeError:
        print(f'{name} is not a string')
