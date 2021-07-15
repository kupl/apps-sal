from itertools import chain

ORTHO = lambda move, i: lambda c: c[i] == move[i] and c[(i+1)%3] == move[(i+1)%3]
DIAG = lambda move, i, s: lambda c: c[i] == (c[(i+1)%3] if s else 3-c[(i+1)%3]) and c[(i+2)%3] == move[(i+2)%3]
CORN = lambda i: lambda c: c[i%3] == c[(i+1)%3] == (3 - c[(i+2)%3] if i else c[(i+2)%3])

def play_OX_3D(moves):
    p = 0
    board = (set(), set())
    for move in moves:
      board[p].add(tuple(move))
      if any(chain(
        (len(list(filter(ORTHO(move, i), board[p]))) == 4 for i in range(3)),
        (len(list(filter(DIAG(move, i, s), board[p]))) == 4 for i in range(3) for s in (0,1)),
        (len(list(filter(CORN(i), board[p]))) == 4 for i in range(3))
        )):
        return '{} wins after {} moves'.format(['O','X'][p], sum(map(len,board)))
      p = 1 - p
    return 'No winner'
