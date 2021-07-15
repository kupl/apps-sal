def say_hello(name, city, state):
    greetName = ''
    for n in name:
        if n == name[-1]:
            greetName += n
            greetName += '!'
        else:
            greetName += n
            greetName += ' '
    return 'Hello, ' + greetName + ' Welcome to ' + city + ', ' + state + '!'
