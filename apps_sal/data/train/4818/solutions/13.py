def solution(a, b):
    p = len(a)
    w = len(b)
    if p > w:
        l = b + a + b
        return l
    else:
        m = a + b + a
        return m
