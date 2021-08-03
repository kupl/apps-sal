def sale_hotdogs(n):
    if n < 5:
        ans = n * 100
    elif n >= 5 and n < 10:
        ans = n * 95
    else:
        ans = n * 90
    return ans
