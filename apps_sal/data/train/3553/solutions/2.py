from re import match, compile


def show_me(name):
    return match(compile('^[A-Z][a-z]+(?:-[A-Z][a-z]+)*$'), name) != None
