def calculator(x, y, op):
    poss_ops = ['+', '-', '*', '/']
    if isinstance(x, str) or isinstance(y, str) or op not in poss_ops:
        ans = 'unknown value'
    else:
        ans = eval(str(x) + op + str(y))
    return ans
