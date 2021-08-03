def black_or_white_key(key_press_count):
    k = ['white', 'black', 'white', 'white', 'black', 'white',
         'black', 'white', 'white', 'black', 'white', 'black']
    return k[(key_press_count - 1) % 88 % 12]
