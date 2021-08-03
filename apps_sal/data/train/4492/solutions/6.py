def hex_color(codes):
    if codes == '':
        return 'black'
    r, g, b = map(int, codes.split(' '))
    if 0 == r == g == b:
        return 'black'
    if r == g == b:
        return 'white'
    if r > g and r > b:
        return 'red'
    if g > r and g > b:
        return 'green'
    if b > g and b > r:
        return 'blue'
    if r > g and r == b:
        return 'magenta'
    if r > b and r == g:
        return 'yellow'
    if b > r and b == g:
        return 'cyan'
