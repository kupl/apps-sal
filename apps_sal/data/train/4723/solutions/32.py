def greet(name): 
    return f'Hello {name.capitalize()}!' #or
    return 'Hello %s!' % name.capitalize() #or
    return 'Hello {}!'.format(name.capitalize())
