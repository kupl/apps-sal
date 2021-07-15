def multiply(n):
    if n<0:
        n = -n
        return -n*5**len(str(n))
    else:
        return n*5**len(str(n))
