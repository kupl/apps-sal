# THanks to easter eggs kata ;*

def height(n, m):
    if n >= m:
        return (2 ** (min(n, m)) - 1)
    f = 1
    res = 0
    for i in range(n):
        f = f * (m - i) // (i + 1)
        res += f
    return res


def solve(emulator):
    m = emulator.drops
    n = emulator.eggs
    h = 0
    tryh = 0
    while n and m:
        tryh = height(n - 1, m - 1) + 1
        if emulator.drop(h + tryh):
            n -= 1
        else:
            h += tryh
        m -= 1
    return(h + 1)
    # continue here
