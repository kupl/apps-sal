def sum_of_minimums(numbers):
    return sum((min(sorted(subarray)) for subarray in numbers))
