def sum_two_smallest_numbers(numbers):
    return sum(sorted(numbers)[:2]) if numbers else None
