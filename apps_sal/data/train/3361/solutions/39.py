def sum_of_minimums(numbers):
    s = 0
    for el in numbers:
        s = s + min(el)
    return s
