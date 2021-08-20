def greet(name):
    a = list(name)[0].upper() + ''.join(list(name)[1:]).lower()
    return 'Hello {}'.format(a) + '!'
