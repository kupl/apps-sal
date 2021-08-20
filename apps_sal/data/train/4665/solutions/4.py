def puzzle_tiles(width, height):
    temp1 = (' ' * 3 + '_( )__ ' * width).rstrip()
    temp2 = ' _' + '     _'.join(['|'] * (width + 1))
    temp3 = '   _ '.join(['(_'] * (width + 1))
    temp4 = ' ' + '__( )_'.join(['|'] * (width + 1))
    temp5 = ' ' + temp2[::-1].rstrip()
    temp6 = '  _' + ' _   _'.join([')'] * (width + 1))
    res = [temp1]
    for i in range(height):
        if i % 2 == 0:
            res.append(temp2)
            res.append(temp3)
            res.append(temp4)
        else:
            res.append(temp5)
            res.append(temp6)
            res.append(temp4)
    return '\n'.join(res)
