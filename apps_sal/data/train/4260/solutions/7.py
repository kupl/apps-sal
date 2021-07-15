def mark_spot(n):
    if not isinstance(n,int):
        return "?"
    if n % 2 == 0 or n < 1:
        return "?"
    res = ""
    demi = n//2
    for i in range(demi):
        for j in range(2*i):
            res += " "
        res += "X"
        for j in range(4*(demi-i) - 1):
            res += " "
        res += "X\n"
    for j in range(2*demi):
        res += " "
    res += "X\n"
    for i in reversed(list(range(demi))):
        for j in range(2*i):
            res += " "
        res += "X"
        for j in range(4*(demi-i) - 1):
            res += " "
        res += "X\n"
    return res

