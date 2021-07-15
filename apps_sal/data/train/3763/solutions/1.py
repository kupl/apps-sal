def calculator(x,y,op):
    try:
        assert op in "+-*/"
        return eval('%d%s%d' % (x, op, y))
    except:
        return "unknown value"
