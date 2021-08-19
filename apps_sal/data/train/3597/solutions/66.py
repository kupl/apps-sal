def say_hello(name, city, state):
    full_name = ' '.join((elt for elt in name))
    return 'Hello, %s! Welcome to %s, %s!' % (full_name, city, state)
