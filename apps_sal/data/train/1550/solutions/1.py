import math


def xnor(num1, num2):
    if num1 < num2:
        temp = num1
        num1 = num2
        num2 = temp
    num1 = togglebit(num1)
    return num1 ^ num2


def togglebit(n):
    if n == 0:
        return 1
    i = n
    n = n | n >> 1
    n |= n >> 2
    n |= n >> 4
    n |= n >> 8
    n |= n >> 16
    return i ^ n


for _ in range(int(input())):
    (a, b, n) = [int(i) for i in input().split()]
    xoro = [a, b, a ^ b]
    xnoro = [a, b]
    index = 2
    while index != 8:
        xnoro.append(xnor(xnoro[index - 1], xnoro[index - 2]))
        index += 1
    if n > 8:
        print(max(xoro[n % 3 - 1], xnoro[n % 3 + 5]))
    else:
        print(max(xoro[n % 3 - 1], xnoro[n - 1]))
