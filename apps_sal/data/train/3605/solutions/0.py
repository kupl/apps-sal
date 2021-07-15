def diagonal(n, p):
    # your code
    res = 0
    for base in range(p, max(n,p) + 1):
        value = 1
        for i in range(base-p+1,base+1):
            value *= i
        for i in range(1,p+1):
            value //= i
        res += int(value)
    return res

