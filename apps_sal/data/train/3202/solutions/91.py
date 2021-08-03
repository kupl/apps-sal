def greet(name, owner):
    if name == owner:
        return "Hello boss"
    else:
        return "Hello guest"


print(greet("paschoal", "paschoal"))
print(greet("paschoal", "morelli"))
