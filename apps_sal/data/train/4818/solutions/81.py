def solution(a, b):
    if len(a) < len(b):
        return a + b + a
    else:
        return b + a + b
