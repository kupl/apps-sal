def say_hello(name, city, state):
    full_name = ''
    for (index, word) in enumerate(name):
        full_name += name[index]
        if index < len(name) - 1:
            full_name += ' '
    text = 'Hello, ' + full_name + '! Welcome to ' + city + ', ' + state + '!'
    return text
