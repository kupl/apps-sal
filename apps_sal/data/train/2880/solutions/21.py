def seven(m):
    steps = 0
    times = 0

    

    while m > 99:
        left = m%10
        m = m//10
        m = m - (int(left) * 2)
        steps = steps + 1
    return (m,steps)
