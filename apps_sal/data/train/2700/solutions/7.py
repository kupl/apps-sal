def black_or_white_key(key_press_count):
    # your code here
    w,b = 'white','black'
    keyboard = [w,b,w,w,b,w,b,w,w,b,w,b]
    return keyboard[(key_press_count - 1) % 88 % 12]

