codes = {
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
    'gold': 5,
    'silver': 10
}

def decode_resistor_colors(bands):
    bands = [codes[band] for band in bands.split()] + [20]
    ohms = (bands[0] * 10 + bands[1]) * 10 ** bands[2]
    p = ''
    for c in 'kM':
        if ohms // 1000:
            ohms /= 1000; p = c
    return '%s%s ohms, %s%%' % (str(ohms).replace('.0', ''), p, bands[3])
