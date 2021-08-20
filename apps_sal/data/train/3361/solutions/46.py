def sum_of_minimums(numbers):
    total_sum = 0
    i = 0
    while i < len(numbers):
        total_sum += min(numbers[i])
        i += 1
    return total_sum
