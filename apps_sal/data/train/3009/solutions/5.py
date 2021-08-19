def pairs(ar):
    return sum((1 for (a, b) in zip(ar[::2], ar[1::2]) if min(a, b) + 1 == max(a, b)))
