def sale_hotdogs(n):
    # your code here
    if n < 5:
        p = 100 * n
    elif n == 0:
        p = 0
    elif (n >= 5) and (n < 10):
        p = 95 * n
    else:
        p = 90 * n
    return p
