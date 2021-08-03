def max_product(lst, n):
    lst = sorted(lst, reverse=True)
    result = lst[0]
    for i in range(1, n):
        result *= lst[i]
    return result
