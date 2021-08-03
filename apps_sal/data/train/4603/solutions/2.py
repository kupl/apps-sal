def Ackermann(m, n):
    return n + 1 if m == 0 else (Ackermann(m - 1, 1) if n == 0 else Ackermann(m - 1, Ackermann(m, n - 1)))
