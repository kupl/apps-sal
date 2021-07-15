def greet(name, owner):
    n = 'boss' if name == owner else 'guest'
    return 'Hello {}'.format(n)
