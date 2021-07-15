def sum_of_minimums(numbers):
    return sum([sorted(x)[0] for x in numbers])
