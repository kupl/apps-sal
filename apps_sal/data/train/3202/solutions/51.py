def greet(name, owner):
    re = ['Hello boss','Hello guest']
    return re[0] if name == owner else re[1]
