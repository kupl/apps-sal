def say_hello(n, c, s):
    b = ''
    for i in range(len(n)):
        b += ' ' + n[i]
    return 'Hello,' + b + '! Welcome to ' + c + ', ' + s + '!'
