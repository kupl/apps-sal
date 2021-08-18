from functools import lru_cache


@lru_cache(maxsize=None)
def highest_floor(eggs, drops):
    """Return the highest floor for the given numbers of eggs and drops"""
    if eggs > drops:
        eggs = drops
    if eggs <= 1:
        return drops if eggs == 1 else 0
    return highest_floor(eggs - 1, drops - 1) + 1 + highest_floor(eggs, drops - 1)


def solve(emulator):
    """Return the least floor for which the egg breaks"""
    drops = emulator.drops
    eggs = emulator.eggs

    lower_bound, n = 0, 0
    while drops > 0:
        n = lower_bound + highest_floor(eggs - 1, drops - 1) + 1
        drops -= 1
        if emulator.drop(n):
            eggs -= 1
            if eggs == 0 or drops == 0:
                return n
        else:
            lower_bound = n
    return n + 1
