def sum_of_minimums(numbers):
    min_sum = int()
    for num in numbers:
        min_sum += min(num)
    return min_sum
