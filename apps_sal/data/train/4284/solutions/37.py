def array_leaders(numbers):
    res = []
    for i in range(len(numbers)):
        if numbers[i] > sum(x for x in numbers[i + 1:]):
            res.append(numbers[i])
    return res
