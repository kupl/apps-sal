d = {'black': 0, 'brown': 1, 'red': 2, 'orange': 3, 'yellow': 4, 'green': 5, 'blue': 6, 'violet': 7, 'gray': 8, 'white': 9, 'silver': 10, 'gold': 5}


def decode_resistor_colors(bands):
    bands = [d[b] for b in bands.split()]
    ohms = (bands[0] * 10 + bands[1]) * 10 ** bands[2]
    (ohms, sfx) = (ohms / 1000000.0, 'M') if ohms > 999999 else (ohms / 1000.0, 'k') if ohms > 999 else (ohms, '')
    return '{}{} ohms, {}%'.format(int(ohms) if ohms // 1 == ohms else ohms, sfx, bands[3] if len(bands) > 3 else 20)
