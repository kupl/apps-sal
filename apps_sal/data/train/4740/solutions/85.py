def row_sum_odd_numbers(n):
    #your code here
    s = 0
    a1 = 1 + n * (n - 1)
    for i in range(n):
        s += a1
        a1 += 2
    return s
