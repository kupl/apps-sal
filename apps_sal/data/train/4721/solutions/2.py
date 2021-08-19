convertToC = {'C': lambda t: t, 'F': lambda t: (t - 32) * 5 / 9, 'K': lambda t: t - 273.15, 'R': lambda t: (t - 491.67) * 5 / 9, 'De': lambda t: 100 - t * 2 / 3, 'N': lambda t: t * 100 / 33, 'Re': lambda t: t * 5 / 4, 'Ro': lambda t: (t - 7.5) * 40 / 21}
convertFromC = {'C': lambda t: t, 'F': lambda t: t * 9 / 5 + 32, 'K': lambda t: t + 273.15, 'R': lambda t: (t + 273.15) * 9 / 5, 'De': lambda t: (100 - t) * 3 / 2, 'N': lambda t: t * 33 / 100, 'Re': lambda t: t * 4 / 5, 'Ro': lambda t: t * 21 / 40 + 7.5}


def convert_temp(temp, from_scale, to_scale):
    return round(convertFromC[to_scale](convertToC[from_scale](temp)))
