def hex_string_to_RGB(h): 
    def hex(_h): return int(_h, 16)
    return {'r': hex(h[1:3]), 'g':hex(h[3:5]), 'b':hex(h[5:7])}
