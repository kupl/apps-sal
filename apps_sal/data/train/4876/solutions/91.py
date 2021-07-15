def hello(name=''):
    name = name.capitalize()
    if name == '':
        return ("Hello, World!")
    else:
        return ("Hello, {}!".format(name))
