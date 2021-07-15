def sum_consecutives(s):
    prev = None
    x = []
    for i in s:
        if i == prev:
            x[-1] += i
        else:
            x.append(i)
        prev = i
    return x
