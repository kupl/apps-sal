def next_happy_year(year):
    while True:
        year += 1
        if len(str(year)) == len(set(str(year))): break
    return year # cant believe this works
