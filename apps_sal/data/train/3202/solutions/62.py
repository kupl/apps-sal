def greet(name, owner):
    # Add code here
    name = name.lower()
    owner = owner.lower()
    if name == owner:
        return 'Hello boss'
    else:
        return 'Hello guest'
