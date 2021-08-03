def sum_of_minimums(numbers):
    here = []
    for el in numbers:
        x = min(el)
        here.append(x)
    return sum(here)
