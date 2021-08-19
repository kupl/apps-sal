def square_up(n):
    sqrList = [0 for _ in range(n * n)]
    for i in range(1, n + 1):
        index = n * i - 1
        for j in range(1, i + 1):
            sqrList[index] = j
            index -= 1
    return sqrList
