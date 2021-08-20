colors = {(1, 0, 0): 'red', (0, 1, 0): 'green', (0, 0, 1): 'blue', (1, 0, 1): 'magenta', (1, 1, 0): 'yellow', (0, 1, 1): 'cyan', (1, 1, 1): 'white'}


def hex_color(codes):
    codes = codes or '0 0 0'
    items = [int(c) for c in codes.split()]
    m = max(items)
    return colors[tuple((i == m for i in items))] if m else 'black'
