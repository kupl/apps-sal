def is_even(number):
    if isinstance(number, float):
        even = False
    else:
        result = number % 2
        even = not result
    return even
