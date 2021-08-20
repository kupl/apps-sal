from math import factorial as f


def nCk(n, k):
    return f(n) // f(k) // f(n - k)


def bouncy_count(x):
    return 10 ** x - (nCk(10 + x, 10) + nCk(9 + x, 9) - 10 * x - 1)
