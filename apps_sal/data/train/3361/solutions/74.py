def sum_of_minimums(numbers):
    x = []
    for i in numbers:
        x.append(min(i))
    return sum(x)
