def difference_of_squares(n):
    arr_pow = []
    two = 0
    for i in range(1, n + 1):
        arr_pow.append(i)
        two += i ** 2
    one = sum(arr_pow)
    return one ** 2 - two
