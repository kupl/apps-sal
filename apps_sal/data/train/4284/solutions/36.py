def array_leaders(numbers):
    o = []
    for (n, i) in enumerate(numbers):
        if i > sum(numbers[n + 1:]):
            o.append(i)
    return o
