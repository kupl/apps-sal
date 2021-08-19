converters = {('C', 'F'): lambda c: c * 9 / 5 + 32, ('C', 'K'): lambda c: c + 273.15, ('C', 'R'): lambda c: (c + 273.15) * 9 / 5, ('C', 'De'): lambda c: (100 - c) * 3 / 2, ('C', 'N'): lambda c: c * 33 / 100, ('C', 'Re'): lambda c: c * 4 / 5, ('C', 'Ro'): lambda c: c * 21 / 40 + 7.5, ('F', 'C'): lambda f: (f - 32) * 5 / 9, ('K', 'C'): lambda k: k - 273.15, ('R', 'C'): lambda r: (r - 491.67) * 5 / 9, ('De', 'C'): lambda de: 100 - de * 2 / 3, ('N', 'C'): lambda n: n * 100 / 33, ('Re', 'C'): lambda re: re * 5 / 4, ('Ro', 'C'): lambda ro: (ro - 7.5) * 40 / 21}


def convert_temp(temp, from_scale, to_scale):
    f = converters.get((from_scale, to_scale))
    x = f(temp) if f else convert_temp(convert_temp(temp, from_scale, 'C'), 'C', to_scale)
    return round(x)
