def two_sum(numbers, target):
    d = {}
    for i, n in enumerate(numbers):
        if target - n in d:
            return [d[target - n], i]
        d[n] = i
