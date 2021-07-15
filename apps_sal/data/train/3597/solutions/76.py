def say_hello(name, city, state):
    name_=''
    for i in name:
        name_+=i+' '
    name_=name_[:-1]
    return 'Hello, {}! Welcome to {}, {}!'.format(name_, city, state)
