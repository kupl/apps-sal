def greet(name, owner):
    if name == owner:
        return "Hello boss"

    else:
        return "Hello guest"


a = 'Daniel'
b = 'Daniel'

print(greet(a, b))
