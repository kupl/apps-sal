for _ in range(int(input())):
    n = int(input())
    n = n * 4 - 1
    xm = 0
    y = 0
    for z in range(n):
        (a, b) = list(map(int, input().split()))
        xm ^= a
        y ^= b
    print(xm, y)
