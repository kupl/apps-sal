def difference_of_squares(n):
    n = range(n + 1)
    new = [i for i in n]
    sum_1 = sum(new) ** 2
    new_x = [i ** 2 for i in n]
    sum_2 = sum(new_x)
    res = sum_1 - sum_2
    print(res)
    return res
