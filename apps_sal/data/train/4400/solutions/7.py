def minimum_steps(numbers, value, s=0):
    for (i, n) in enumerate(sorted(numbers)):
        s += n
        if s >= value:
            return i
