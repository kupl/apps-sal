def sum_of_minimums(numbers):
    return sum((min((i for i in l)) for l in numbers))
