def solution(a, b):
    ab = ''
    if len(a) < len(b):
        ab = a + b + a
    else:
        ab = b + a + b
    return ab
