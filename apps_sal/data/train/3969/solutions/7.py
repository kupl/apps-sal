def graceful_tipping(bill):
    total = bill * 1.15
    if total < 10:
        total = int(total) + (total % 1 > 0)
    else:
        x = len(str(int(total))) - 2
        m = 5 * 10 ** x
        total = (int(total / m) + (total % m > 0)) * m
    return total
