def lostSheep(friday,saturday,total):
    weekend_total = sum(friday) + sum(saturday)
    difference = total - weekend_total
    return difference
