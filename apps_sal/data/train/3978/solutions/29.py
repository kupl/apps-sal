def check_for_factor(base, factor):
    m = []
    for i in range(1, base + 1):
        if base % i == 0:
            m.append(i)
    return factor in m
