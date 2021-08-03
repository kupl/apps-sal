def per(n):
    if n < 10:
        return []
    l = []
    while n > 9:
        total = 1
        num = str(n)
        for i in num:
            total *= int(i)
        l.append(total)
        n = total
    return l
