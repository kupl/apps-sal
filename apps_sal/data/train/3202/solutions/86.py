def greet(name, owner):
    a = 'boss' if name == owner else 'guest'
    return 'Hello {}'.format(a)
