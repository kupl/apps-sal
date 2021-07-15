def halving_sum(n):
    start = n
    total = 0
    while start >= 1:
        total += start
        start = int(start / 2)
    return total
