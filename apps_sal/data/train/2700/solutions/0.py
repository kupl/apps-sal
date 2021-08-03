def black_or_white_key(key_press_count):
    return "black" if (key_press_count - 1) % 88 % 12 in [1, 4, 6, 9, 11] else "white"
