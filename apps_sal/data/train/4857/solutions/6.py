def square_up(n):
    a = []
    for j in range(1,n+1):
        for i in range(n, j, -1):
            a.append(0)
        for i in range(j, 0, -1):
            a.append(i)
    return a

