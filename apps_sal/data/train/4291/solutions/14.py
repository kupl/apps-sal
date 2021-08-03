def century(year):
    for i in range(year):
        if year in range((i * 100) + 1, (i + 1) * 100 + 1):
            return i + 1
