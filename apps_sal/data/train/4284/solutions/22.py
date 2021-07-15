def array_leaders(numbers):
    n = 0
    out = []
    for i in reversed(numbers):
        if i > n:  out.append(i)
        n += i
    out.reverse()
    return out
