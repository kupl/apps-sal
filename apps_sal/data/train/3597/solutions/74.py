def say_hello(name, city, state):

    new_name = ''

    for x in name:
        if x != name[-1]:
            new_name += (x + ' ')

        else:
            new_name += x

    return 'Hello, ' + new_name + '! Welcome to ' + city + ', ' + state + '!'
