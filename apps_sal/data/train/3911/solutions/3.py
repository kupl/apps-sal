from math import ceil

# All the solutions I saw were so slow, iterating the whole m -> n
# For M, the solutions are the 37 + 63k in [m, n]
# You can find that with chinese remainder theorem, or just by looking at the examples
# Then just calculate B and C for each
# No need to waste time doing useless loops


def howmuch(m, n):
    m, n = min(m, n), max(m, n)
    x = max(0, ceil((m - 37) / 63))
    return [[f"M: {y}", f"B: {(y-2)//7}", f"C: {(y-1)//9}"] for y in range(37 + 63 * x, n + 1, 63)]
