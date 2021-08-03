def solution(a, b):
    if len(a) > len(b):
        s = b + a + b
    elif len(a) < len(b):
        s = a + b + a
    return s
