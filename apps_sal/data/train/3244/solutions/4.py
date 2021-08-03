d = {40: 3.85, 20: 1.93, 10: 0.97, 5: 0.49, 1: 0.10}


def cheapest_quote(n):
    papers, total = 40, 0
    while n > 0:
        if n >= papers:
            total += d[papers] * (n // papers)
            n %= papers
        if papers > 5:
            papers //= 2
        else:
            papers = 1
    return round(total, 2)
