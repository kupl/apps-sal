def seven(m):
    count = 0
    while m >= 100:
        count += 1
        m = int(str(m)[:-1]) - 2 * int(str(m)[-1])
    return m, count
