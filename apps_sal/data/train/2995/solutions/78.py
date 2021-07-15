def sum_mul(n, m):
    if n <= 0 or m <= 0:
        return 'INVALID'
    else:
        new_arr = []
        for num in range(n, m, n):
            new_arr.append(num)
        return sum(new_arr)
