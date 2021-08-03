def solution(a, b):
    if len(a) > len(b):
        x = b + a + b
    else:
        x = a + b + a
    return x
