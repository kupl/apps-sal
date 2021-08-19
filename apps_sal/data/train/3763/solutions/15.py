def calculator(x, y, op):
    if op not in ['+', '/', '-', '*']:
        return 'unknown value'
    else:
        try:
            a = str(x) + op + str(y)
            return eval(a)
        except:
            return 'unknown value'
