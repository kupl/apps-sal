def puzzle_tiles(w, h):
    puzzle = ['  ' + ''.join([' _( )__'] * w)]
    for i in range(h):
        if i % 2:
            puzzle.append(''.join([' |_    '] * (w + 1)))
            puzzle.append(''.join(['  _) _ '] * (w + 1))[:-2])
        else:
            puzzle.append(''.join([' _|    '] * (w + 1)))
            puzzle.append(''.join(['(_   _ '] * (w + 1))[:-2])
        puzzle.append(' ' + ''.join(['|__( )_'] * (w + 1))[:-6])
    return '\n'.join((l.rstrip() for l in puzzle))
