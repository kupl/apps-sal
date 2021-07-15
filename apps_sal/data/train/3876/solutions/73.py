def find(n):
    return sum([x for x in range(1,n+1, 1) if (x/3).is_integer() or (x/5).is_integer()])
