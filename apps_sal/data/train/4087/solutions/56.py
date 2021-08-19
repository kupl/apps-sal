def get_char(c):
    if c < 0 or c > 255:
        print('ASCII out of range')
        return -1
    return chr(c)
