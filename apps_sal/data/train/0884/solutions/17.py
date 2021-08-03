for _ in range(int(input())):
    X, R = map(int, input().split())
    a = []
    b = []
    for i in range(2, X + 1):
        if X % i == 0:
            a.append(i**R)
    for j in range(2, R + 1):
        if R % j == 0:
            b.append(j * X)
    print(sum(a), sum(b))
