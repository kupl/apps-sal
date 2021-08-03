def greet(name, owner):
    return 'Hello ' + 'boss' * (name == owner) + 'guest' * (name != owner)
