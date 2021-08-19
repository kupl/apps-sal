def greet(name, owner):
    result = ''
    if name == owner:
        result = 'Hello boss'
    else:
        result = 'Hello guest'
    return result
