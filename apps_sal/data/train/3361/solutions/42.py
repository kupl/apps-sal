def sum_of_minimums(numbers):
    count = []
    for n in numbers:
        count.append(min(n))
    return sum(count)
