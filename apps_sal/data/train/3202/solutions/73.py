def greet(name, owner):
    return 'Hello {0}'.format('guest' if name != owner else 'boss')
