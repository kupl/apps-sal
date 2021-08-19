def seven(m):
    licznik = 0
    m = str(m)  # change into string because int isn't iterable
    while len(str(m)) > 2:
        m = str(m)  # in each iteration it should be string
        m = int(m[:-1]) - int(m[-1]) * 2
        licznik += 1
    return int(m), licznik
