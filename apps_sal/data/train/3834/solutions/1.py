def palin(a,b):
    s = str(10**((a-1)//2) + b-1)
    return int(s+s[::-1][a%2:])
