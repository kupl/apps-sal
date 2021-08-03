def calculator(x, y, op):

    try:
        dic = {'+': y + x, '-': x - y,
               '*': y * x, '/': x / y}

        return dic[op]

    except:
        return 'unknown value'
