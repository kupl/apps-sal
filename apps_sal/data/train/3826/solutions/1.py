def cycle(n):
    if not n % 2 or not n % 5:
        return -1
    (x, mods) = (1, set())
    while x not in mods:
        mods.add(x)
        x = 10 * x % n
    return len(mods)
