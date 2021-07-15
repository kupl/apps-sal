def hello(name='World'):
    if name == None or name == '':
        return 'Hello, World!'
    else:
        return 'Hello, ' + str(name.lower().capitalize()) + '!'
