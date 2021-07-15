def hex_string_to_RGB(hex_string): 
    integer = eval(f'0x{hex_string.lstrip("#").lower()}')
    return {'r': (integer >> 16) & 255, 'g': (integer >> 8) & 255, 'b': integer & 255}
