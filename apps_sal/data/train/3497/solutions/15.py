def isPP(n):
    for i in range(2, 400):
        for j in range(2, 50):
            if i ** j == n:
                return [i, j]
    return None
