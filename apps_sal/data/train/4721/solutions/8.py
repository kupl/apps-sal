def convert_temp(tt, f, t):
    if f == 'C':
        x = tt
    if f == 'F':
        x = (tt - 32) * 5.0 / 9
    if f == 'K':
        x = tt - 273.15
    if f == 'R':
        x = (tt - 491.67) * 5.0 / 9
    if f == 'De':
        x = 100 - tt * 2.0 / 3
    if f == 'N':
        x = tt * 100.0 / 33
    if f == 'Re':
        x = tt * 5.0 / 4
    if f == 'Ro':
        x = (tt - 7.5) * 40.0 / 21

    if t == 'C':
        y = x
    if t == 'F':
        y = x * 9.0 / 5 + 32
    if t == 'K':
        y = x + 273.15
    if t == 'R':
        y = (x + 273.15) * 9.0 / 5
    if t == 'De':
        y = (100 - x) * 3.0 / 3
    if t == 'N':
        y = x * 33.0 / 100
    if t == 'Re':
        y = x * 4.0 / 5
    if t == 'Ro':
        y = x * 21.0 / 40 + 7.5

    return round(y)
