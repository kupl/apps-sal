def max_tri_sum(numbers):
    x = sorted(set(numbers))
    l = []
    for n in reversed(x):
        if len(l) <= 2:
            l.append(n)
    return sum(l)
