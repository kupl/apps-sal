def greet(name, owner):
    r = 'Hello guest'
    if name == owner:
        r = 'Hello boss'
    return r
