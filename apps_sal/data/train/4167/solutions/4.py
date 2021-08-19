from math import factorial


def binomial(m, n):
    return factorial(n) / factorial(m) / factorial(n - m)


def descriptions(arr):
    count = 0
    for i in range(1, len(arr)):
        if arr[i] == arr[i - 1] + 1:
            count += 1
    return 2 ** count
