def say_hello(name, city, state):
    string = ''.join([str(i) + ' ' for i in name])
    string_neu = string[:-1]
    city = str(city)
    state = str(state)
    return 'Hello, ' + string_neu + '! Welcome to ' + city + ', ' + state + '!'
