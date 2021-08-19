def seven(m):
    print(m)
    steps = 0
    while m >= 100:
        steps += 1
        y = m % 10
        x = m // 10
        print(m)
        m = x - 2 * y
    return (int(m), steps)
