def zeros(n):
    if n == 0:
        return 0
    else:
        return int(n / 5) + int(zeros(n / 5))
