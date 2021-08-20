def which_note(key_press_count):
    black_key = [2, 5, 7, 10, 12, 14, 17, 19, 22, 24, 26, 29, 31, 34, 36, 38, 41, 43, 46, 48, 50, 53, 55, 58, 60, 62, 65, 67, 70, 72, 74, 77, 79, 82, 84, 86]
    dict_white = {1: 'A', 3: 'B', 4: 'C', 6: 'D', 8: 'E', 9: 'F', 11: 'G', 13: 'A', 15: 'B', 16: 'C', 18: 'D', 20: 'E', 21: 'F', 23: 'G', 25: 'A', 27: 'B', 28: 'C', 30: 'D', 32: 'E', 33: 'F', 35: 'G', 37: 'A', 39: 'B', 40: 'C', 42: 'D', 44: 'E', 45: 'F', 47: 'G', 49: 'A', 51: 'B', 52: 'C', 54: 'D', 56: 'E', 57: 'F', 59: 'G', 61: 'A', 63: 'B', 64: 'C', 66: 'D', 68: 'E', 69: 'F', 71: 'G', 73: 'A', 75: 'B', 76: 'C', 78: 'D', 80: 'E', 81: 'F', 83: 'G', 85: 'A', 87: 'B', 88: 'C'}
    if key_press_count % 88 == 0:
        return 'C'
    elif key_press_count % 88 in black_key:
        return str(dict_white[(key_press_count - 1) % 88]) + '#'
    else:
        return str(dict_white[key_press_count % 88])
