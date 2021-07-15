def greet(name): 
    name = name.lower()
    a = name[0].upper()
    b = list(name)
    b.pop(0)
    b = ''.join(b)
    final = a + b
    return 'Hello ' + final + '!'
    pass
