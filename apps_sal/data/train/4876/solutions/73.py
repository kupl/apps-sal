def hello(name=''):
    if name == '' or type(name) != str:
        return 'Hello, World!'
    else:
        final_name = name[0].upper() + name[1:].lower()
        return 'Hello, ' + final_name + '!'
