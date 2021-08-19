BANDS = {'black': 0, 'brown': 1, 'red': 2, 'orange': 3, 'yellow': 4, 'green': 5, 'blue': 6, 'violet': 7, 'gray': 8, 'white': 9}
TOLERANCE_BAND = {'gold': 5, 'silver': 10}
LETTERS = {0: '', 1: 'k', 2: 'M'}
PATTERN = '{}{} ohms, {}%'


def decode_resistor_colors(bands):
    (first, second, third, *fourth) = bands.split(' ')
    ohms = (BANDS[first] * 10 + BANDS[second]) * 10 ** BANDS[third]
    count = 0
    while ohms >= 1000:
        ohms /= 1000
        count += 1
    ohms = int(ohms) if int(ohms) == ohms else ohms
    letter = LETTERS[count]
    if fourth:
        tolerance = TOLERANCE_BAND[fourth[0]]
    else:
        tolerance = 20
    return PATTERN.format(ohms, letter, tolerance)
