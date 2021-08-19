def greet(name):
    name = name.lower()
    return 'Hello ' + name[0].upper() + name[1:] + '!'


print(greet('BILLY'))
