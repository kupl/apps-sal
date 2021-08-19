def sum_of_minimums(a):
    m = []
    for i in a:
        m.append(min(i))
    return sum(m)
