def one_down(txt):
    if type(txt) != str:
        return 'Input is not a string'
    abc = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    result = ''
    for x in txt:
        if x not in abc:
            result += x
        elif x in 'aA':
            result += 'zZ'['aA'.index(x)]
        else:
            result += abc[abc.index(x) - 1]
    return result
