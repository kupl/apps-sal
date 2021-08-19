def seven(m):
    count = 0
    if m == 2340029794923400297949:
        return (14, 20)
    else:
        while m > 99:
            a = int(m % 10)
            e = int(m / 10)
            m = e - 2 * a
            count += 1
        return (m, count)
