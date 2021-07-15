def solution(a, b):
    if len(a) > len(b):
        return "".join(b + a + b)
    elif len(a) < len(b):
        return "".join(a + b + a)

