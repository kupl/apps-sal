def hex_string_to_RGB(hex_string):
    return {'r': int(f'0x{hex_string[1:3]}', 16), 'g': int(f'0x{hex_string[3:5]}', 16), 'b': int(f'0x{hex_string[5:]}', 16)}
