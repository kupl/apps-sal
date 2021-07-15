def hex_color(codes):
    if codes in ('', '000 000 000'):
                        return 'black'
    r, g, b = (int(color) for color in codes.split())
    if r == g == b:     return 'white'
    if r > g and r > b: return 'red'
    if g > r and g > b: return 'green'    
    if b > r and b > g: return 'blue'
    if r == b:          return 'magenta'
    if g == r:          return 'yellow'
    if b == g:          return 'cyan'
