def encode_resistor_colors(ohms_string):
    s = str(get_num_ohms(ohms_string))
    ohms = s[:2]
    tolerance = str(len(s[2:]))
    color_bands = [get_color(ohms[0]), get_color(ohms[1]), get_color(tolerance), 'gold']
    return ' '.join(color_bands)


def get_num_ohms(s):
    n = s.split(' ')[0]
    multiplier = 1000 if n[-1] == 'k' else 1000000 if n[-1] == 'M' else 1
    f = float(n[:-1]) * multiplier if multiplier > 1 else float(n)
    return int(f)


def get_color(n):
    color_map = {
        '0': 'black',
        '1': 'brown',
        '2': 'red',
        '3': 'orange',
        '4': 'yellow',
        '5': 'green',
        '6': 'blue',
        '7': 'violet',
        '8': 'gray',
        '9': 'white'
    }
    return color_map[n]
