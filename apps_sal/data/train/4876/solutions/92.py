def hello(name=''):
    if name =='':
        txt = 'Hello, World!'
        return txt
    elif len(name) == 1:
        naam = name.upper()
        txt = f'Hello, {naam}!'
    elif len(name) > 1:
        naam = name[0].upper() + name[1:].lower()
        txt = f'Hello, {naam}!'
    else:
        txt = 'Hello, World!'
        return txt
    return txt

