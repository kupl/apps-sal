# from math import copysign
def sequence_sum(a, b, step):
    n = (b - a) // step
    return 0 if n < 0 else (n + 1) * (n * step + a + a) // 2
