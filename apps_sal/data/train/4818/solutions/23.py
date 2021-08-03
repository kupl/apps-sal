def solution(a, b):

    if len(a) > len(b):
        d = a
        c = b
    else:
        d = b
        c = a
    return f"{c}{d}{c}"
