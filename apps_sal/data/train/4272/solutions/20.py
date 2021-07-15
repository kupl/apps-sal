'''def greet(name):
    if name == "Johnny":
        return "Hello, my love!"
    return "Hello, {name}!".format(name=name)'''
greet=lambda n:{"Johnny":"Hello, my love!"}.get(n,"Hello, {}!".format(n))
