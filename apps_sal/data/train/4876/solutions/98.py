def hello(name=''):
    return "Hello, World!" if name == '' else "Hello, " + name[0].upper() + name[1:len(name)].lower() + "!"
