def array_leaders(numbers):
    n = sum(numbers)
    out = []
    for i in numbers:
        n -= i
        if i > n:
            out.append(i)
    return out
