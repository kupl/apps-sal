def difference_of_squares(n):
    a = list(range(1, n + 1))
    s1 = sum(a) ** 2
    arr = [el ** 2 for el in a]
    s2 = sum(arr)
    return s1 - s2
