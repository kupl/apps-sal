def lamps(a):
    i, count = 0, 0

    for lamp in a:
        if lamp == i % 2:
            count += 1
        i += 1

    return min(count, i - count)
