def max_number(n):
    s = str(n)
    l = [int(x) for x in s]
    l = sorted(l,reverse=True)
    m = len(l) - 1
    return sum([y*(10**(m - i)) for i,y in enumerate(l)])
