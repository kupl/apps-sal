Dict = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7}


def toCoord(position):
    if type(position) != str:
        return []
    if position[0] in Dict and (1 <= int(position[1]) <= 8):
        return (Dict[position[0]], int(position[1]) - 1)


def fromCoord(position):
    return chr(64 + position[0] + 1) + str(position[1] + 1)


def available_moves(position):
    try:
        if type(position) == str and len(position) == 2 and 65 <= ord(position[0]) <= 90:
            moves = []
            position = toCoord(position)
            if position == []:
                return moves
            if 0 <= position[0] <= 7 and 0 <= position[1] <= 7:
                i = 1
                for x in range(8):
                    if (x, position[1]) != position:
                        moves.append(fromCoord((x, position[1])))

                for y in range(8):
                    if (position[0], y) != position:
                        moves.append(fromCoord((position[0], y)))

                for i in range(1, max(max((7 - position[0]), (position[0])), max((7 - position[1], position[1]))) + 1):
                    if 0 <= position[0] + i <= 7 and 0 <= position[1] + i <= 7:
                        moves.append(fromCoord((position[0] + i, position[1] + i)))

                    if 0 <= position[0] + i <= 7 and 0 <= position[1] - i <= 7:
                        moves.append(fromCoord((position[0] + i, position[1] - i)))

                    if 0 <= position[0] - i <= 7 and 0 <= position[1] + i <= 7:
                        moves.append(fromCoord((position[0] - i, position[1] + i)))

                    if 0 <= position[0] - i <= 7 and 0 <= position[1] - i <= 7:
                        moves.append(fromCoord((position[0] - i, position[1] - i)))

                return sorted(moves)
            return []
        return []
    except TypeError:
        return []


print(available_moves("D8"))
