def greet(name): 
    res = 'Hello ' + name[0].upper()
    for i in range(1, len(name)):
        res += name[i].lower()
    return res + '!'
