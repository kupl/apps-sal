def next_happy_year(year):
    return next((y for y in range(year + 1, 9877) if len(set(str(y))) == 4))
