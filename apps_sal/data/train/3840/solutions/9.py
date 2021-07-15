def largest_power(n):
    if n == 1:
        return 0, -1
    for i in range(n - 1, 1, -1):
        k = sum(round(i ** (1 / e)) ** e == i for e in range(2, i.bit_length()))
        if k != 0:
            return i, k
    return 1, -1
