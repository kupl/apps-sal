def greet(name, owner):
    if name == owner:
        result = 'boss'
    else:
        result = 'guest'
    return 'Hello ' + result
