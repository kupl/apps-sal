def black_or_white_key(key_press_count):
    w = "white"
    b = "black"
    repetitive_keyboard_layout = [w, b, w, w, b, w, b, w, w, b, w, b,]
    return repetitive_keyboard_layout[(key_press_count - 1) % 88 % 12]

