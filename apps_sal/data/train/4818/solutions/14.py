def solution(a, b):
    if a and b.isnumeric():
        return b + a + b if a > b else a + b + a
    else:
        return b + a + b if len(a) > len(b) else a + b + a
