def solution(a, b):
    lsta = []
    lstb = []
    if a and b == int:
        if a < b:
            return a + b + a
        else:
            return b + a + b
    else:
        for x in a:
            lsta.append(x)
        for y in b:
            lstb.append(y)
        if len(lsta) < len(lstb):
            r1 = ''.join(lsta)
            r2 = ''.join(lstb)
            return r1 + r2 + r1
        else:
            r1 = ''.join(lsta)
            r2 = ''.join(lstb)
            return r2 + r1 + r2
