def max_product(lst, n):
    a = sorted(lst, reverse=True)
    ans = 1
    for i in range(0, n):
        ans *= a[i]
    return ans
