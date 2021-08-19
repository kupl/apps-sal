import numpy as np
t = int(input())
while t:
    n = int(input())
    X = []
    Y = []
    for i in range(n):
        (x, y) = map(int, input().split())
        (x, y) = (x - y, x + y)
        X.append(x)
        Y.append(y)
    X = set(X)
    Y = set(Y)
    if len(X) == n - 1 or len(Y) == n - 1:
        print(0)
    else:
        X = list(X)
        Y = list(Y)
        X.sort()
        Y.sort()
        for i in range(len(X) - 1):
            X[i] = X[i + 1] - X[i]
        X = X[:-1]
        for i in range(len(Y) - 1):
            Y[i] = Y[i + 1] - Y[i]
        Y = Y[:-1]
        print(min(min(X) / 2.0, min(Y) / 2.0))
    t -= 1
