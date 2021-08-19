def sum_two_smallest_numbers(numbers):
    # your code here
    number = numbers  # lol
    number.sort(reverse=True)
    a = number.pop()
    b = number.pop()
    return a + b
