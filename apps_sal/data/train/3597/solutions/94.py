def say_hello(name, city, state):
    name_join = ' '.join([x for x in name])
    sentence = 'Hello, {}! Welcome to {}, {}!'.format(name_join, city, state)
    return sentence
