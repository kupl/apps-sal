def power_of_two(x):
    i = 1
    l = [1]
    while i < x:
        i *= 2
        l.append(i)
    return x in l
