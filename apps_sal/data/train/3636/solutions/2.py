def bouncy_ratio(percent):
    if percent <= 0 or percent >= 99:
        raise
    bouncy, i = 0, 99
    while float(bouncy) / i < percent:
        i += 1
        bouncy += sum(any(f(a, b) for a, b in zip(str(i), str(i)[1:])) for f in [lambda x, y: x > y, lambda x, y: x < y]) == 2
    return i
