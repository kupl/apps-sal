def greet(name, owner):
    # Add code here
    r = 'Hello guest'
    if name == owner:
        r = 'Hello boss'
    return r

