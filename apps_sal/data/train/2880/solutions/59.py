def seven(m):
    counter = 0
    while len(str(m)) > 2:
        counter += 1
        a = int(str(m)[:-1])
        b = int(str(m)[-1:])
        m = a - b * 2
    return (m, counter)
