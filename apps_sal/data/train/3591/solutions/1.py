def doors(n):
    doors = [False] * n
    for i in range(0, n):
        for j in range(i, n, i + 1):
            doors[j] = not doors[j]
    return doors.count(True)
