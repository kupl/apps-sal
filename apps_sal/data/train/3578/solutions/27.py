def paperwork(n, m):
    return n * m if all((x > 0 for x in (n, m))) else 0
