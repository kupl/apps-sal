def puzzle_tiles(width, height):

    top = '   ' + ' '.join(['_( )__'] * width)
    bottom = ' |' + '|'.join(['__( )_'] * width) + '|'
    rows = [top]

    for i in range(height):
        if i % 2:
            line1 = ' |_' + '|_'.join(['     '] * width) + '|_'
            line2 = '  _)' + '_)'.join([' _   '] * width) + '_)'
        else:
            line1 = ' _|' + '_|'.join(['     '] * width) + '_|'
            line2 = '(_' + '(_'.join(['   _ '] * width) + '(_'

        rows.append('\n'.join([line1, line2, bottom]))

    return '\n'.join(rows)
