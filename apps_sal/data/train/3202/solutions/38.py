def greet(name, owner):
    if name == owner:
        what = 'boss'
    else:
        what = 'guest'
    return 'Hello {}'.format(what)
