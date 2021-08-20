def solution(a, b):
    return a * (len(a) < len(b)) + b + a + b * (len(a) > len(b))
