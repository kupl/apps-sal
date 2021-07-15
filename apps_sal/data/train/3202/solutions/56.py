def greet(name, owner):
    if name != owner:
        return 'Hello guest'
    elif owner == name:
        return 'Hello boss'

