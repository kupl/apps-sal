def century(year):
    q, r = divmod(year, 100)
    return q + bool(r)

