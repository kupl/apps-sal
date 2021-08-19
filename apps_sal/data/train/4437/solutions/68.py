def cookie(x):
    WHOATETHECOOKIE = ''
    if x == str(x):
        WHOATETHECOOKIE = 'Zach!'
    elif x == bool(x):
        WHOATETHECOOKIE = 'the dog!'
    else:
        WHOATETHECOOKIE = 'Monica!'
    return 'Who ate the last cookie? It was ' + WHOATETHECOOKIE
