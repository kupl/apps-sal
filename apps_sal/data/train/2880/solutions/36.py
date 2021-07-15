def seven(m):
    count = 0
    while m > 99:
        m = int(str(m)[:-1]) - 2 * int(str(m)[-1])
        count += 1
    return (m, count)
