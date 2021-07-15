def max_number(n):
    l=sorted(list(map(int,str(n))),reverse=True)
    return int(''.join(str(x) for x in l))
