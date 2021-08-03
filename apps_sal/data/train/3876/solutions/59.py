def find(n):
    tot = 0

    for i in range(3, n + 1, 3):
        tot += i

    for j in range(5, n + 1, 5):
        tot += j

    if n > 14:
        for j in range(15, n + 1, 15):
            tot -= j

    return tot
