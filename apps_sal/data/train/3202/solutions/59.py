def greet(name, owner):
    greeting = 'boss' if name == owner else 'guest'
    return 'Hello {greeting}'.format(greeting=greeting)
