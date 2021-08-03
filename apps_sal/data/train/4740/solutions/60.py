def row_sum_odd_numbers(n):
    startnr = n * n - (n - 1)
    sum = 0
    for i in range(startnr, startnr + n * 2, 2):
        sum += i
    return sum
