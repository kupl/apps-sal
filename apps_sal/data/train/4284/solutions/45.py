def array_leaders(numbers):
    length = len(numbers)
    numbers.append(0)
    res = []
    for i in range(length):
        if numbers[i] > sum(numbers[i + 1:]):
            res.append(numbers[i])
    return res
