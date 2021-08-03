def solution(a, b):
    if len(a) > len(b):
        short_long = b + a + b
    else:
        short_long = a + b + a
    return short_long
