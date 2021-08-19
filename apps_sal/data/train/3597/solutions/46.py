def say_hello(name, city, state):
    strname = ' '.join((str(x) for x in name))
    return 'Hello, ' + strname + '! Welcome to ' + str(city) + ', ' + str(state) + '!'
