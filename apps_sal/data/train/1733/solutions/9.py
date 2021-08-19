letter_to_number = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8}


def possible_moves(p1):
    possible_moves = ([1, 2], [-1, 2], [1, -2], [-1, -2], [2, 1], [-2, 1], [2, -1], [-2, -1])
    new_positions = []
    for move in possible_moves:
        if 0 < p1[0] + move[0] <= 8 and 0 < p1[1] + move[1] <= 8:
            new_positions.append([p1[0] + move[0], p1[1] + move[1]])
    return new_positions


def knight(p1, p2):
    new_p1 = [letter_to_number[p1[0]], int(p1[1])]
    new_p2 = [letter_to_number[p2[0]], int(p2[1])]
    if new_p2 in possible_moves(new_p1):
        return 1
    for move1 in possible_moves(new_p1):
        if new_p2 in possible_moves(move1):
            return 2
            break
    for move1 in possible_moves(new_p1):
        for move2 in possible_moves(move1):
            if new_p2 in possible_moves(move2):
                return 3
    for move1 in possible_moves(new_p1):
        for move2 in possible_moves(move1):
            for move3 in possible_moves(move2):
                if new_p2 in possible_moves(move3):
                    return 4
    for move1 in possible_moves(new_p1):
        for move2 in possible_moves(move1):
            for move3 in possible_moves(move2):
                for move4 in possible_moves(move3):
                    if new_p2 in possible_moves(move4):
                        return 5
    return 6
