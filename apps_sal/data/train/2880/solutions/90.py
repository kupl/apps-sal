def seven(m):
    result = m
    count = 0
    while len(str(int(result))) > 2:
        y = result % 10
        result = result // 10

        result = result - 2 * y
        count += 1

    return (result, count)
