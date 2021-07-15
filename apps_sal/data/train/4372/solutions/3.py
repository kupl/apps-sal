def lostSheep(friday, saturday, total):
    return total - sum(saturday) - sum(friday)
