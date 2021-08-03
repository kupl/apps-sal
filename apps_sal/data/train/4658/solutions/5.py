def max_product(lst, n, res=1):
    for i in sorted(lst)[-n:]:
        res *= i
    return res
