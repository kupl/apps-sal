def faulty_odometer(n):
    return sum('012356789'.index(c) * 9**i for i, c in enumerate(str(n)[::-1]))
