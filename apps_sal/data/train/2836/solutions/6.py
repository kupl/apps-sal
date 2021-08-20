def find_screen_height(width, ratio):
    r = list(map(int, ratio.split(':')))
    return f'{width}x{width * r[1] // r[0]}'
