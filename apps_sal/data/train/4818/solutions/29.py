def solution(a, b):
    x = len(a)
    y = len(b)
    if x >= y:
        return b + a + b
    else:
        return a + b + a
