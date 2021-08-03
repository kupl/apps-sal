def odd_count(n):
    count = 0
    if n % 2 == 0:
        count = n - (n / 2)
    else:
        count = ((n + 1) - (n + 1) / 2) - 1
    return count
