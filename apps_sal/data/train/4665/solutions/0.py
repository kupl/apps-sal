def puzzle_tiles(width, height):

    def f():
        yield ('  ' + ' _( )__' * width)
        for i in range(height):
            if i % 2 == 0:
                yield (' _|' + '     _|' * width)
                yield ('(_' + '   _ (_' * width)
                yield (' |' + '__( )_|' * width)
            else:
                yield (' |_' + '     |_' * width)
                yield ('  _)' + ' _   _)' * width)
                yield (' |' + '__( )_|' * width)
    return '\n'.join(f())
