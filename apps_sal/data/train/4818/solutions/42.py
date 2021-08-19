def solution(a, b):
    if len(a) < len(b):
        new_string = a + b + a
    else:
        new_string = b + a + b
    return new_string
