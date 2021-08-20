def greet(name):
    result = name[0].upper()
    for i in range(1, len(name)):
        result += name[i].lower()
    return 'Hello ' + result + '!'
