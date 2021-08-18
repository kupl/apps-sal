def fib_digits(n):
    numCount = [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [0, 6], [0, 7], [0, 8], [0, 9]]
    a, b = 1, 1
    for i in range(n - 1):
        a, b = b, a + b
    fib_list = list(str(a))
    i = 0
    while i < len(fib_list):
        numCount[int(fib_list[i])][0] += 1
        i += 1
    i = 0
    while i < len(numCount):
        numCount[i] = tuple(numCount[i])
        if numCount[i][0] == 0:
            numCount.pop(i)
        else:
            i += 1
    return sorted(numCount, key=lambda x: (x[0], x[1]), reverse=True)
