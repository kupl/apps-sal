from math import ceil, log10


def graceful_tipping(bill):
    bill *= 1.15
    if bill < 10:
        return ceil(bill)
    e = int(log10(bill))
    unit = (10 ** e) / 2
    return ceil(bill / unit) * unit
