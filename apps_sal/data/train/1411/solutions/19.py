import math


def fun(X, R, A, B):
    if A > B:
        if (X * (A - B)) % A == 0:
            return max((X * (A - B) // A) - 1, 0)
        else:
            return X * (A - B) // A
    elif B > A:
        if (X * (B - A)) % B == 0:
            return max((X * (B - A) // B) - 1, 0)
        else:
            return X * (B - A) // B
    else:
        return 0


for _ in range(int(input())):
    X, R, A, B = list(map(int, input().strip().split()))
    print(fun(X, R, A, B))
