def greet(name):
    if name == "Johnny":
        return "Hello, my love!"
    else:
        return f"Hello, {name}!".format(name=name)

g = greet('Johnny')
print(g)
