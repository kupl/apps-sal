def seven(m):
    steps = 0
    while m >= 100:
        print(m)
        x = m // 10
        y = m % 10
        m = x - y * 2
        steps += 1
    return (int(m), steps)
