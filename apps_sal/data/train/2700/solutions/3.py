keyboard = [("white", "black")[int(n)] for n in "010010100101"]


def black_or_white_key(key_press_count):
    return keyboard[(key_press_count - 1) % 88 % 12]
