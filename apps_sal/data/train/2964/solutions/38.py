def sum_two_smallest_numbers(numbers):
    a, b = numbers[:2]
    for i in range(2, len(numbers)):
        a, b, c = sorted((a, b, numbers[i]))
    return a + b
