from itertools import cycle
def puzzle_tiles(width, height):
    up_puzzle = ''.join(['  ',  ' _( )__'*width, '\n'])
    puzzle = cycle(
    [
    ['', ' _|    '*width,  ' _|'],
    ['', '(_   _ '*width,   '(_'],
    [' ', '|__( )_'*width,   '|'],
    [' ','|_     '*width,   '|_'],
    [' ',' _) _  '*width,  ' _)'],
    [' ','|__( )_'*width,    '|']
    ])
    return up_puzzle  +  '\n'.join('{}{}{}'.format(*next(puzzle)) for i in range(height*3))
