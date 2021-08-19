def calculator(x, y, op):
    try:
        if op not in '+-*/' or type(x) != int or type(y) != int:
            raise TypeError
        else:
            return eval('%d%s%d' % (x, op, y))
    except:
        return 'unknown value'
