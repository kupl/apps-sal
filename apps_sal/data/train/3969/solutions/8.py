from math import ceil


def graceful_tipping(bill):
    total = bill * 1.15
    if total < 10:
        return ceil(total)
    total /= 5
    d = 0
    while total >= 20:
        d += 1
        total /= 10
    return ceil(total) * 5 * 10**d
