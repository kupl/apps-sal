def greet(name):
    a = lambda m: "Hello, my love!" if m == "Johnny" else "Hello, {}!".format(m)
    return a(name)
