import math


def togglebit(n):

    if (n == 0):
        return 1
    i = n
    n = n | (n >> 1)
    n |= n >> 2
    n |= n >> 4
    n |= n >> 8
    n |= n >> 16

    return i ^ n


def xnor(num1, num2):

    if (num1 < num2):
        temp = num1
        num1 = num2
        num2 = temp
    num1 = togglebit(num1)

    return num1 ^ num2


def x(A, B, N):
    if N == 1:
        return A
    elif N == 2:
        return B
    else:
        t0 = A ^ B
        t1 = B ^ t0
        t2 = t0 ^ t1
        if N % 3 == 0:
            return t0
        elif N % 3 == 1:
            return t1
        else:
            return t2


def xn(A, B, N):
    if N == 1:
        return A
    elif N == 2:
        return B
    else:
        cache = [xnor(A, B)]
        cache.append(xnor(cache[0], B))
        for i in range(2, 7):
            cache.append(xnor(cache[i - 1], cache[i - 2]))
        t1 = xnor(cache[6], cache[5])
        t2 = xnor(cache[6], t1)
        t0 = xnor(t2, t1)
        if N <= 9:
            return cache[N - 3]
        else:
            if N % 3 == 0:
                return t0
            elif N % 3 == 1:
                return t1
            else:
                return t2


t = int(input())
for _ in range(t):
    p, q, n = map(int, input().split())
    print(max(x(p, q, n), xn(p, q, n)))
