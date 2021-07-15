def do_math(s) :
    
    res = operator = 0
    for op in (x for y in 'abcdefghijklmnopqrstuvwxyz' for x in s.split() if y in x):
        op = int(''.join(x for x in op if x.isdigit()))
        if not res:
            res += op
            continue
        if operator == 0:
            res += op
            operator += 1
        elif operator == 1:
            res -= op
            operator += 1
        elif operator == 2:
            res *= op
            operator += 1
        else:
            res /= op
            operator = 0
        
    return round(res)
