from copy import copy
move_map = ((-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1))

def algebraic_to_eucledian(pos):
    return (int(pos[1]) - 1, 'abcdefgh'.index(pos[0]))

def knight(p1, p2):
    p1, p2 = algebraic_to_eucledian(p1), algebraic_to_eucledian(p2)
    num_moves = -1
    visited = []
    moves = [p1]
    while moves:
        next_moves = []
        num_moves += 1
        for move in moves:
            if move == p2:
                return num_moves
            visited.append(move)
            next_moves.extend([(move[0]+x, move[1]+y) for x, y in move_map if 0 <= move[0]+x < 8 and 0 <= move[1]+y < 8 and (move[0]+x, move[1]+y) not in visited])
        moves = copy(next_moves)

