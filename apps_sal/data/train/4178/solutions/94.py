def min_sum(l):
    l = sorted(l)
    backward = reversed(l)
    forward = iter(l)
    length = len(l)
    result = 0
    for (i, (f, b)) in enumerate(zip(forward, backward)):
        if i < length / 2:
            print(f, b)
            result += f * b
    return result
