def seven(m, count=0):
    if len(str(m)) <= 2:
        return (m, count)
    else:
        count += 1
        return seven(m // 10 - 2 * (m % 10), count)
