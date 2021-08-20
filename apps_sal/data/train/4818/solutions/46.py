def solution(a, b):
    a1 = len(a)
    b1 = len(b)
    if a1 > b1:
        return b + a + b
    else:
        return a + b + a
