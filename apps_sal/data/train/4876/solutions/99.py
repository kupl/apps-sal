def hello(name='World'):
    if len(name) == 0:
        return 'Hello, World!'
    else:
        new_name = name[0].upper() + name[1:].lower()
        return 'Hello, ' + new_name + '!'
