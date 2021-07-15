def sum_of_minimums(numbers):
    x = 0
    for lst in numbers:
        x += min(lst)
    return x
