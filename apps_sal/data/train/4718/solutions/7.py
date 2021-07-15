def x(n):
    return [
        [int(i == j or i+j == n-1) for j in range(n)]
        for i in range(n)
    ]
