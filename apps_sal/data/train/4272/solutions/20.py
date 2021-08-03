'''def greet(name):
    if name == "Johnny":
        return "Hello, my love!"
    return "Hello, {name}!".format(name=name)'''


def greet(n): return {"Johnny": "Hello, my love!"}.get(n, "Hello, {}!".format(n))
