def say_hello(name, city, state):
    res = 'Hello, '
    for n in name:
        res += n + ' '
    res = res[:-1]
    res += '! Welcome to '
    res += city + ', '
    res += state + '!'
    return res
