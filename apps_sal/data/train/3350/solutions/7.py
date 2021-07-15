def hex_string_to_RGB(hex_string):
    color = int(hex_string[1:], 16)
    return {'r': color >> 16 & 255, 'g': color >> 8 & 255, 'b': color & 255}
