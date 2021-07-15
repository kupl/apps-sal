def black_or_white_key(c):
    i = int('010100101010'[((c - 1) % 88 - 3) % 12])
    return ['white', 'black'][i]
