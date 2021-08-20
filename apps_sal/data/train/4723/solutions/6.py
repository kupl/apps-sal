def greet(name):
    lst = []
    lst.append(name[0].upper())
    for i in range(len(name) - 1):
        lst.append(name[i + 1].lower())
    return 'Hello ' + ''.join(lst) + '!'
