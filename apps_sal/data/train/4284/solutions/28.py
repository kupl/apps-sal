def array_leaders(numbers):
    john = []
    for i, v in enumerate(numbers):
        if v > sum(numbers[i + 1:]):
            john.append(v)
    return john
