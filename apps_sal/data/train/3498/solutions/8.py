COLOR_CODE = {
    'silver': 10,
    'gold': 5,

    'black': 0,
    'brown': 1,
    'red': 2,
    'orange': 3,
    'yellow': 4,
    'green': 5,
    'blue': 6,
    'violet': 7,
    'gray': 8,
    'white': 9,
}

DEFAULT_TOLERANCE = 20


def decode_resistor_colors(bands):
    bands = [COLOR_CODE[band] for band in bands.split()] + [DEFAULT_TOLERANCE]

    value = bands[0] * 10 + bands[1]
    multiplier = bands[2]
    tolerance = bands[3]

    exponent = multiplier + 1

    if exponent >= 6:
        letter = 'M'
        exponent -= 6
    elif exponent >= 3:
        letter = 'k'
        exponent -= 3
    else:
        letter = ''

    value *= 10 ** (exponent - 1)

    return '{:g}{} ohms, {}%'.format(value, letter, tolerance)
