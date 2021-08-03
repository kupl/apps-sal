def halving_sum(n):
    divisor = 1
    addends = []
    addend = n // divisor
    while addend > 0:
        addends.append(addend)
        divisor *= 2
        addend = n // divisor
    return sum(addends)
