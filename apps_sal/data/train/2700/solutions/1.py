w, b = "white", "black"
keyboard = [w, b, w, w, b, w, b, w, w, b, w, b]


def black_or_white_key(count):
    return keyboard[(count - 1) % 88 % 12]
