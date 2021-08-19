def solution(a, b):
    (a, b) = sorted([a, b], key=len)
    return a + b + a
