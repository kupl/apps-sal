def does_fred_need_houseboat(x, y):
    r = 0
    year = 0
    while x ** 2 + y ** 2 > r ** 2:
        area = 3.1415 * r ** 2 + 100.0
        r = (area / 3.1415) ** 0.5
        year += 1
    return year
