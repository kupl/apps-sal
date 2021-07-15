def array_leaders(numbers):
    out, s = [], 0
    for i in reversed(range(len(numbers))):
        if numbers[i] > s:
            out.insert(0, numbers[i])
        s += numbers[i]
    return out
