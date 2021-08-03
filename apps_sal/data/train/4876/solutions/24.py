def hello(name='World'):
    return 'Hello, %s!' % (name + int(not bool(name)) * 'World').capitalize()
