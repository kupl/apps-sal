def greet(name, owner):
    greet = 'guest'
    if name == owner:
        greet = 'boss'
    return 'Hello ' + greet
