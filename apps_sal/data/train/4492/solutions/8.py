def hex_color(codes):
    if codes == "":
        return 'black'
    r_, g_, b_ = map(int, codes.split())
    r, g, b, = max(r_, g_, b_) == r_, max(r_, g_, b_) == g_, max(r_, g_, b_) == b_

    if (r_, g_, b_) == (0, 0, 0):
        return 'black'
    elif r and g and b:
        return 'white'
    elif r and g:
        return 'yellow'
    elif r and b:
        return 'magenta'
    elif g and b:
        return 'cyan'
    elif r:
        return 'red'
    elif g:
        return 'green'
    elif b:
        return 'blue'
