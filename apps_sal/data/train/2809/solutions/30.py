def digitize(n):
    arr = []
    result = n

    shouldGo = True

    while shouldGo:
        arr.append(result % 10)

        result = result // 10

        if result == 0:
            shouldGo = False

    return arr
