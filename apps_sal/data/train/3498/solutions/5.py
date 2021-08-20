def decode_resistor_colors(bands):
    bands_lst = bands.split(' ')
    VALUES = {'black': 0, 'brown': 1, 'red': 2, 'orange': 3, 'yellow': 4, 'green': 5, 'blue': 6, 'violet': 7, 'gray': 8, 'white': 9, 'gold': 5, 'silver': 10}
    first = VALUES[bands_lst[0]]
    second = VALUES[bands_lst[1]]
    num = str(first) + str(second)
    ohms = int(num) * pow(10, VALUES[bands_lst[2]])
    unit = ' ohms'
    tolerance = 20
    if len(bands_lst) > 3:
        tolerance = VALUES[bands_lst[3]]
    if ohms in range(0, 999):
        unit = ' ohms'
    elif ohms in range(1000, 999999):
        ohms = ohms / 1000
        unit = 'k ohms'
    elif ohms >= 1000000:
        ohms = ohms / 1000000
        unit = 'M ohms'
    return '{:g}{}, {}%'.format(ohms, unit, tolerance)
