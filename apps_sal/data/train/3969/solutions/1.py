import math
def graceful_tipping(bill):
    c = bill * 115 / 100
    m = 1 if c < 10 else 5 * 10 ** int(math.log10(c) - 1)
    return math.ceil(c / m) * m

