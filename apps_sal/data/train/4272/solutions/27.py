def greet(name):
    def a(m): return "Hello, my love!" if m == "Johnny" else "Hello, {}!".format(m)
    return a(name)
