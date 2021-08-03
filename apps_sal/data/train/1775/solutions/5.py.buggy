import itertools as it

rows = tuple (it.permutations (list(range(1,5))))

visibles = [{r:reduce (lambda (m,s),e: (e,1+s) if e > m else (m,s), r,       (r[ 0],1))[1] for r in rows},
            {r:reduce (lambda (m,s),e: (e,1+s) if e > m else (m,s), r[::-1], (r[-1],1))[1] for r in rows}]

def matches (puzzle, clues):
    return (    all (clues[15-i] == visibles[0][      puzzle [i]] for i in range(4) if clues[15-i] > 0)
            and all (clues[ 4+i] == visibles[1][      puzzle [i]] for i in range(4) if clues[ 4+i] > 0)
            and all (clues[   i] == visibles[0][list(zip(*puzzle))[i]] for i in range(4) if clues[   i] > 0)
            and all (clues[11-i] == visibles[1][list(zip(*puzzle))[i]] for i in range(4) if clues[11-i] > 0))

def valid (puzzle):
    return all (r in rows for r in zip (*puzzle))

def solve_puzzle (clues):
    return next (puzzle for puzzle in it.product (rows, repeat=4) if valid (puzzle) and matches (puzzle, clues))

