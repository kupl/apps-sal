def paperwork(n, m):
    if n <= 0 or m <= 0:
        return 0
    elif n > 0 and m > 0:
        pages = n * m
        return pages
