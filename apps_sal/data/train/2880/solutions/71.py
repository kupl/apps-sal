def seven(m):
    licznik = 0
    m = str(m)
    while len(str(m)) > 2:
        m = str(m)
        m = int(m[:-1]) - int(m[-1]) * 2
        licznik += 1
    return (int(m), licznik)
