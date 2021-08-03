def row_sum_odd_numbers(n):
    min = n**2 - n + 1
    max = n**2 + n - 1
    sum = 0
    while min <= max:
        if min % 2 == 1:
            sum = sum + min
            min += 2
    return sum
