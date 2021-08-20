def solution(n):
    x = divmod(n, 0.5)
    if x[1] < 0.25:
        return x[0] * 0.5
    else:
        return x[0] / 2 + 0.5
