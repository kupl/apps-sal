def better_than_average(c, y):
    cp = 0
    for i in c:
        cp += i
    cp = cp / len(c)
    return y >= cp
