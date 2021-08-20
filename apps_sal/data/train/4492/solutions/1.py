_COLORS = ['black', 'blue', 'green', 'cyan', 'red', 'magenta', 'yellow', 'white']


def hex_color(codes):
    colors = [int(color) for color in (codes or '0 0 0').split()]
    index = int(''.join(('1' if color and color == max(colors) else '0' for color in colors)), 2)
    return _COLORS[index]
