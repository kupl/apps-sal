def hello(name=None):
    if name is None:
        return 'Hello, World!'
    elif name == '':
        return 'Hello, World!'
    else:
        lower_name = name.lower()
        cap_name = lower_name.capitalize()
        return 'Hello, ' + cap_name + '!'
