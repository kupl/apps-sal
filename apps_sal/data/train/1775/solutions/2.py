import numpy as np

# check if n appears more than once in array


def duped(l):
    for e in l:
        if l.count(e) > 1:
            return True
    return False

# find empty square to place number


def find_empty(city):
    for r in range(4):
        for c in range(4):
            if city[r][c] == 0:
                return (r, c)

# check if clue works with n of skycrapers seen


def check_clue(clue, counter):
    if clue == 0:
        return True
    return counter == clue

# check how many skyscrapers can be seen and if they are ok with clues


def vis(arr, clues):
    l = len(arr)
    a1 = 0
    a2 = 0
    counter1 = 0
    counter2 = 0
    # count skycrapers visible from the two sides
    for k in range(l):
        if arr[k] > a1:
            a1 = arr[k]
            counter1 += 1
        if arr[l - k - 1] > a2:
            a2 = arr[l - k - 1]
            counter2 += 1
    # if the arr is not filled yet can't count the clues
    if l < 4:
        return True
    # check the clues
    return check_clue(clues[0], counter1) and check_clue(clues[1], counter2)

# check if a n placed is ok with all the clues


def is_valid(r, c, city, clues):
    #row and column
    row = [h for h in city[r] if h != 0]
    col = [r[c] for r in city if r[c] != 0]
    # if numbers are duplicate return
    if duped(row) or duped(col):
        return False
    # top right bottom left clues
    tc, rc, bc, lc = [clues[k][c] if k % 2 == 0 else clues[k][r] for k in range(4)]
    # check if all clues work
    return vis(row, (lc, rc)) and vis(col, (tc, bc))

# recursive function


def solve(city, clues):
    # find position of empty square
    pos = find_empty(city)
    # if there is no empty square then it's solved
    if not pos:
        return True
    #row and column
    r, c = pos
    # all numbers that you can put in a 4x4
    for n in range(1, 5):
        # put number in city
        city[r][c] = n
        # check if it's good
        if is_valid(r, c, city, clues):
            # recursion trigger
            if solve(city, clues):
                return True
        # delete number if it doesn't work cause of backtracking or just not valid
        city[r][c] = 0
    # if no possible solution :
    return False

# initial function


def solve_puzzle(clues):
    # list of clues with the last 2 reversed to make indexing easy
    clues = [list(clues[k:k + 4]) if k < 5 else list(reversed(clues[k:k + 4])) for k in range(0, 13, 4)]  # top right bottom left
    # initialize city matrix
    city = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    # solve
    solve(city, clues)
    return tuple([tuple(a) for a in city])
