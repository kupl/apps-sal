def solution(a, b):
    result = ''
    if len(a) < len(b):
        result = a + b + a
    else:
        result = b + a + b
    return result
    pass
