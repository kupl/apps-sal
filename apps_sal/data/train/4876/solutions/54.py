def hello(name=''):
    if len(name.strip()) == 0:
        return 'Hello, World!'
    else:
        a = name.title()
        return 'Hello, ' + a + '!'
