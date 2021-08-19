def century(year):
    (value, remainder) = divmod(year, 100)
    return value + 1 if remainder else value
