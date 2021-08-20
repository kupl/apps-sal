def greet(name, owner):
    if name == owner:
        greeting = 'boss'
    else:
        greeting = 'guest'
    return 'Hello {0}'.format(greeting)
