def say_hello(name, city, state):
    
    txt1 = 'Hello, {} {} {}! Welcome to {}, {}!'
    txt2 = 'Hello, {} {}! Welcome to {}, {}!'
    txt3 = 'Hello, {} {} {} {}! Welcome to {}, {}!'
    
    
    l = len(name)
    
    if l == 3:
        return txt1.format(name[0], name[1], name[2], city, state)
    elif l == 4:
        return txt3.format(name[0], name[1], name[2], name[3], city, state)
    else:
        return txt2.format(name[0], name[1], city, state)
