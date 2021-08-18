
def transformChessPointToMatrixPoint(point):
    return [int(ord(point[0]) - 96), int(point[1])]


def availableMoves(point):
    moves = []
    final_moves = []
    moves.append([point[0] + 2, point[1] + 1])
    moves.append([point[0] + 2, point[1] - 1])
    moves.append([point[0] - 2, point[1] + 1])
    moves.append([point[0] - 2, point[1] - 1])
    moves.append([point[0] + 1, point[1] + 2])
    moves.append([point[0] + 1, point[1] - 2])
    moves.append([point[0] - 1, point[1] + 2])
    moves.append([point[0] - 1, point[1] - 2])

    for move in moves:
        if 1 <= move[0] <= 8 and 1 <= move[1] <= 8:
            final_moves.append(move)
    return final_moves


def knight(p1, p2):
    p1 = transformChessPointToMatrixPoint(p1)
    p2 = transformChessPointToMatrixPoint(p2)
    already_visited = [p1]

    to_check = [[p1, 0]]

    while len(to_check) > 0:

        if to_check[0][0] == p2:
            return to_check[0][1]

        moves_to_visit = availableMoves(to_check[0][0])
        for move in moves_to_visit:
            if move in already_visited:
                pass
            else:
                already_visited.append(move)
                to_check.append([move, to_check[0][1] + 1])
        to_check.pop(0)
    return None
