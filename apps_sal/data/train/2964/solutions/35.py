def sum_two_smallest_numbers(numbers):
    m1 = min(numbers)
    ind = numbers.index(min(numbers))
    numbers[ind] = max(numbers)
    m2 = min(numbers)
    numbers[ind] = m1
    return m1+ m2
