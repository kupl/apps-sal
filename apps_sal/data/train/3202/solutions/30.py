def greet(name, owner):
    if(name == owner):
        x = 'boss'
    else:
        x = 'guest'
    return "Hello {}".format(x);
