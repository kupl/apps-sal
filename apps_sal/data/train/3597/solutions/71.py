def say_hello(name, city, state):
    a=' '.join(name)+'!'
    r= 'Hello, '+str(a) +' Welcome to {}, {}!'.format(city,state)
    return ''.join(r)
