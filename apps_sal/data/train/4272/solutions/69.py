def greet(name):
    name = name if name != 'Johnny' else 'my love'
    return "Hello, {name}!".format(name=name)
