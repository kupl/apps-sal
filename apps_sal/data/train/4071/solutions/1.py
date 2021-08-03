def next_happy_year(year):
    for n in range(year + 1, 9999):
        if len(set(str(n))) == 4:
            return n
