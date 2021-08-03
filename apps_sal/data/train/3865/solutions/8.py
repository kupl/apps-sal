def looper(start, stop, number):
    c, r, s = 0, [], (stop - start) / (number - (1 if number > 1 else 0))
    while c < number:
        r.append(start + c * s)
        c += 1
    if number > 1:
        r.pop()
        r.append(stop)
    return r
