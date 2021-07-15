def solution(a, b):
    along = len(a)
    blong = len(b)
    return a + b + a if along < blong else b + a + b
