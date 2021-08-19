def arithmetic(a, b, op):
    trans = {'add': '+', 'subtract': '-', 'divide': '/', 'multiply': '*'}
    if type(a) == type(b) == int and op in trans.keys():
        return eval(f'{a}{trans[op]}{b}')
