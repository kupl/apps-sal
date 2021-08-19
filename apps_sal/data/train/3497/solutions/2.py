def isPP(n):
    for i in range(2, n + 1):
        for j in range(2, n + 1):
            if i ** j > n:
                break
            elif i ** j == n:
                return [i, j]
    return None
