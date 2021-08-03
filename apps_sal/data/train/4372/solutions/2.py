def lostSheep(friday, saturday, total):
    sheeps = friday + saturday
    return total - sum(sheeps)
