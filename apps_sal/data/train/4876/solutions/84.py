def hello(name='World'):
    # I don't understand why 'World' default name doesn't work here (it does locally), so I neet to add those two lines
    if not name:
        name = 'World'
    return 'Hello, ' + name.title() + '!'
