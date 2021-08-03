def lostSheep(friday, saturday, total):
    sheep = 0
    for num in friday:
        sheep += num
    for num in saturday:
        sheep += num
    return total - sheep
