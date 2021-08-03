a_len = 0
b_len = 0


def solution(a, b):
    a_len = len(a)
    b_len = len(b)
    if a_len < b_len:
        return a + b + a
    else:
        return b + a + b
