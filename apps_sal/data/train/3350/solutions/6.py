def hex_string_to_RGB(hex_string):
    r, g, b = [ int(hex_string[i:i+2], 16) for i in (1, 3, 5) ]
    return {'r': r, 'g': g, 'b': b}
