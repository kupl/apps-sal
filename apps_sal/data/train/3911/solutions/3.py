from math import ceil


def howmuch(m, n):
    m, n = min(m, n), max(m, n)
    x = max(0, ceil((m - 37) / 63))
    return [[f"M: {y}", f"B: {(y-2)//7}", f"C: {(y-1)//9}"] for y in range(37 + 63 * x, n + 1, 63)]
