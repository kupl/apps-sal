color_map = {0: 'black', 1: 'red', 2: 'green', 3: 'yellow', 4: 'blue', 5: 'magenta', 6: 'cyan', 7: 'white'}


def hex_color(codes):
    (values, brightest, color, i) = ([], 0, 0, 0)
    if not codes:
        codes = '000 000 000'
    for code in codes.split(' '):
        value = int(code)
        if value > brightest:
            brightest = value
            color = 2 ** i
        elif value == brightest != 0:
            color += 2 ** i
        i += 1
    return color_map[color]
