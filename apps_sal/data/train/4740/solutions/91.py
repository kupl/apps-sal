def row_sum_odd_numbers(n):
    odd_number = n * (n - 1) + 1
    odd_numbers = []
    if n == 1:
        return n
    for idx in range(n):
        odd_numbers.append(odd_number)
        odd_number += 2
    return sum(odd_numbers)
