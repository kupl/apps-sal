def solution(a, b):
    new_str = ''
    if len(a) < len(b):
        new_str += a + b + a
    else:
        new_str += b + a + b
    return new_str
