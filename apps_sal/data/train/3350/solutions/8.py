def hex_string_to_RGB(hex_string):
    n = int(hex_string[1:], 16)
    return {'r': n >> 16, 'g': n >> 8 & 255, 'b': n & 255}
