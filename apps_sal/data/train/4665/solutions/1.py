def puzzle_tiles(width, height):
    def line(i):
        if i == 0:
            return '  ' + ' _( )__' * width
        if i % 3 == 0:
            return ' ' + '__( )_'.join('|' for _ in range(width + 1))
        if i % 6 == 1:
            return ' ' + '     '.join('_|' for _ in range(width + 1))
        if i % 6 == 2:
            return '   _ '.join('(_' for _ in range(width + 1))
        if i % 6 == 4:
            return ' ' + '     '.join('|_' for _ in range(width + 1))
        if i % 6 == 5:
            return ' _ '.join('  _)' for _ in range(width + 1))

    return '\n'.join(line(i) for i in range(3 * height + 1))
