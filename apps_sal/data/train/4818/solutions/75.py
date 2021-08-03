def solution(a, b):
    A_length = len(a)
    B_length = len(b)
    if A_length <= B_length:
        return a + b + a
    else:
        return b + a + b
