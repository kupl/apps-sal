def sum_of_minimums(numbers):
    z = []
    for x in numbers:
        z.append(min(x))
    return sum(z)
