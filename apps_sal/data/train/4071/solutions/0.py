def next_happy_year(year):
    year += 1
    while len(set(str(year))) != 4:
        year += 1
    return year
