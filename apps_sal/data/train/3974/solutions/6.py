def two_count(n):
    if n % 2 != 0:
        return 0
    else:
        return 1 + two_count(n // 2)
