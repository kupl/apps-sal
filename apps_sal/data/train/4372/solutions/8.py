def lostSheep(friday,saturday,total):
    s = total - (sum(friday) + sum(saturday))
    return s
