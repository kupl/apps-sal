def find_screen_height(width, ratio):
    r = ratio.split(':')
    return f'{width}x{int(width * int(r[1]) / int(r[0]))}'
