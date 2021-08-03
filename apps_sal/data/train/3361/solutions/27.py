def sum_of_minimums(numbers):
    results = []
    for x in numbers:
        results.append(sorted(x)[0])
    return sum(results)
