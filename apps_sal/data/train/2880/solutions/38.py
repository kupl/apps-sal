def seven(m):
    remain = m
    count = 0
    while remain >= 100:
        x = int(remain / 10)
        y = remain - (x * 10)
        remain = x - (2 * y)
        count += 1
    return remain, count
