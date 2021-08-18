from sys import stdin
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


for _ in range(int(stdin.readline())):
    a, b, n = list(map(int, stdin.readline().split()))
    X = [a, b, a ^ b]
    E = [a, b]
    for i in range(2, n):
        E.append(xnor(E[-1], E[-2]))
        if E[-3:] == E[-6:-3]:
            break
    x = (n - 1) % 3
    e = (n - len(E)) % 3
    if e == 0:
        e = -1
    elif e == 1:
        e = -3
    else:
        e = -2
    print(max(X[x], E[e]))
