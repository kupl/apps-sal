def sum_two_smallest_numbers(numbers):
    # your code here
    numbers.sort()
    subNumbers = numbers[:2]
    return sum(subNumbers)
