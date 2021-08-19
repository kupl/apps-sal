def greet(name):
    if name == None:
        return None
    if name == '':
        return None
    n = len(name)
    if n >= 1:
        return 'hello' + ' ' + name + '!'
