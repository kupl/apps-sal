def hello(name='World'):
    name = name.lower()
    return 'Hello, ' + name.title() + '!' if name != '' else 'Hello, World!'
