def cookie(x):
    template = 'Who ate the last cookie?'
    if type(x) is str:
        return template + ' It was Zach!'
    elif type(x) is float or type(x) is int:
        return template + ' It was Monica!'
    else:
        return template + ' It was the dog!'
