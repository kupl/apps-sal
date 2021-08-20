def say_hello(name, city, state):
    name = ' '.join(name)
    return 'Hello, %(name)s! Welcome to %(city)s, %(state)s!' % vars()
