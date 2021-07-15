def odd_count(n):
    n = round(n)
    if not n%2:
        return n / 2
    else:
        return (n - 1) / 2
