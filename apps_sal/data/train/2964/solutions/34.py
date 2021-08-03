def sum_two_smallest_numbers(numbers):
    for item in numbers:
        if item < 0:
            numbers.remove(item)
    return sum(sorted(numbers)[:2])
