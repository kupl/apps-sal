def sum_of_minimums(numbers):
    result = []
    for (counter, value) in enumerate(numbers):
        num = min(numbers[counter])
        result.append(num)
    return sum(result)
