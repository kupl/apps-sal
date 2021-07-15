def interest(p,r,n):
    simple = p + p * r * n
    while n > 0:
        n -= 1
        p += p * r
    return [round(simple), round(p)]
