def array_leaders(numbers):
    res = []
    for i, value in enumerate(numbers):
        if numbers[i] > sum(numbers[i+1::]):
            res.append(value)
    return res
