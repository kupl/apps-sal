def sum_two_smallest_numbers(numbers):
    number = numbers
    number.sort(reverse=True)
    a = number.pop()
    b = number.pop()
    return a + b
