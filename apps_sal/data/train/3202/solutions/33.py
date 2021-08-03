def greet(name, owner):
    if name == owner:
        return "Hello boss"
    else:
        return "Hello guest"


x = greet('Greg', 'Daniel')
print(x)
