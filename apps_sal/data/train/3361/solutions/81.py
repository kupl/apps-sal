def sum_of_minimums(numbers):
    return sum((sorted(numbers[i])[0] for i in range(len(numbers))))
