def solution(a, b):
    if len(a) < len(b):
        list = a, b, a
    else:
        list = b, a, b
    return "".join(list)
