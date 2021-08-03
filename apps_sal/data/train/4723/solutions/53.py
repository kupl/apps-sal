def greet(name):
    lower = name.lower()
    capital = name[0].upper()
    return ('Hello ' + capital + lower[1:] + "!")
