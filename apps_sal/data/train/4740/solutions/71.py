def row_sum_odd_numbers(n):
    # your code here
    first = 1 + (n * (n - 1))
    sum = 0
    for i in range(n):
        sum = sum + first
        first += 2
    return sum
