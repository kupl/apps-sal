code = {'black': 0, 'brown': 1, 'red': 2, 'orange': 3, 'yellow': 4,
'green': 5, 'blue': 6, 'violet': 7, 'gray': 8, 'white': 9,
'gold': 5, 'silver': 10, '': 20}
def decode_resistor_colors(bands):
    colors = (bands + ' ').split(' ')
    value = 10 * code[colors[0]] + code[colors[1]]
    value *= 10 ** code[colors[2]]
    tolerance = code[colors[3]]
    prefix = ''
    for p in 'kM':
        if value // 1000:
            prefix = p
            value /= 1000
    return "%g%s ohms, %d%%" % (value, prefix, tolerance)

