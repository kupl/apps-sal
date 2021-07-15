def hello(name=''):
    if name != '' or len(name) != 0:
        name = name.lower() + "!"
        name = "Hello, " + name.capitalize()
        print(name)
        return name
    else:
        return 'Hello, World!'
