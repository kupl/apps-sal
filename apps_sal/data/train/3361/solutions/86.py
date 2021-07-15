def sum_of_minimums(numbers):
    a = list()
    for i in numbers:
        a.append(min(i))
    return sum(a)
