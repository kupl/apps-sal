def next_happy_year(year):
    y = year + 1
    while len(str(y)) != len(set(str(y))):
        y += 1
    return y
