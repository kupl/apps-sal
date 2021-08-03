def find(n):
    # Code here
    a = 0
    for i in range(3, n + 1):
        if i % 3 == 0:
            a += i
        elif i % 5 == 0:
            a += i
    return a
