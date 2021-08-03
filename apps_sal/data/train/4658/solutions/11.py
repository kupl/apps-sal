def max_product(lst, n):
    a = lst.sort(reverse=True)
    i = 0
    sum = 1
    while i < n:
        sum = sum * lst[i]
        i += 1
    return sum
