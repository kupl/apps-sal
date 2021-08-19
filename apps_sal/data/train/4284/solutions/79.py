def array_leaders(numbers):
    results = []
    for (i, n) in enumerate(numbers):
        if i < len(numbers) - 1 and sum(numbers[i + 1:]) < n:
            results.append(n)
        elif i == len(numbers) - 1 and n > 0:
            results.append(n)
    return results
