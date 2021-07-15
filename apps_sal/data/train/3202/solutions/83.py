def greet(name, owner):
    if name == owner:
        return('Hello boss')
    if name != owner:
        return('Hello guest')
    else:
        return None
    
greet('Bob','Bob')
