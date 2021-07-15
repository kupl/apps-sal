def say_hello(name, city, state):
    full_name = ''
    for i in range(len(name)):
        full_name +=name[i]+' '
    if full_name[-1] ==' ':
        full_name = full_name[:-1]
    return 'Hello, {}! Welcome to {}, {}!'.format(full_name, city, state)
