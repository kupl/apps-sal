def A(x, n):
    return x * ((n - 1) // x * ((n - 1) // x + 1)) // 2


def solution(n):
    return A(3, n) + A(5, n) - A(15, n)
