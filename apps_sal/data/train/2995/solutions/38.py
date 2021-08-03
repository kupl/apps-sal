def sum_mul(n, m):
    if n <= 0 or m <= 0:
        return "INVALID"

    try:
        return sum(range(n, m, n))
    except:
        return "INVALID"
