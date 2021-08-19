def greet(name, owner):
    if name == owner:
        print('Hello boss')
        return 'Hello boss'
    if name != owner:
        print('Hello guest')
        return 'Hello guest'
