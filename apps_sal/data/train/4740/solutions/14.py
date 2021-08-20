def row_sum_odd_numbers(n):
    (sum, sum2, h, k, i, s1, s2) = (0, 0, n - 1, -1, 0, 0, 0)
    while n != 0:
        sum += n
        n -= 1
    while h != 0:
        sum2 += h
        h -= 1
    while i <= sum - 1:
        if i == sum2:
            s2 = s1
        k += 2
        s1 += k
        i += 1
    return s1 - s2
