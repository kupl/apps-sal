def solution(a, b):
    n1, n2 = len(a), len(b)
    if n1 < n2:
        return a + b + a
    else:
        return b + a + b
