def Horizontal(position):
    R = position[1]
    HorizontalMoves = ["A" + R, "B" + R, "C" + R, "D" + R, "E" + R, "F" + R, "G" + R, "H" + R]
    possible = list(filter(lambda x: (x != position), HorizontalMoves))
    return possible


def Vertical(position):
    F = position[0]
    VerticalMoves = [F + str(1), F + str(2), F + str(3), F + str(4), F + str(5), F + str(6), F + str(7), F + str(8)]
    p = list(filter(lambda y: (y != position), VerticalMoves))
    return p


def TRtBL(position):
    moves = []
    num = int(position[1])
    ASC_Letter = ord(position[0])
    Up = num
    Down = num
    TempLetter = ASC_Letter
    TempLetter2 = ASC_Letter
    while TempLetter < 72 and Up < 8:
        if position[0] == "H" or Up == 8:
            break
        TempLetter = TempLetter + 1
        Up = Up + 1
        moves.append(chr(TempLetter) + str(Up))
    while TempLetter2 > 65 and Down > 0:
        if position[0] == "A" or Down == 1:
            break
        TempLetter2 = TempLetter2 - 1
        Down = Down - 1
        moves.append(chr(TempLetter2) + str(Down))
    return moves


def TLtBR(position):
    moves = []
    num = int(position[1])
    ASC_Letter = ord(position[0])
    Up = num
    Down = num
    TempLetter = ASC_Letter
    TempLetter2 = ASC_Letter
    while TempLetter < 72 and Down > 1:
        if position[0] == "H":
            break
        TempLetter = TempLetter + 1
        Down = Down - 1
        moves.append(chr(TempLetter) + str(Down))
    while TempLetter2 > 65 and Up < 8:
        if position[0] == "A":
            break
        TempLetter2 = TempLetter2 - 1
        Up = Up + 1
        moves.append(chr(TempLetter2) + str(Up))
    return moves


def available_moves(position):
    answer = []
    if not position:
        return answer
    if not isinstance(position, str):
        return answer
    if len(position) != 2:
        return answer
    if int(position[1]) < 1 or int(position[1]) > 8:
        return answer
    if position[0].isdigit():
        return answer
    if ord(position[0]) > 72:
        return answer
    '
    '
    '
    answer.extend(Horizontal(position))
    answer.extend(Vertical(position))
    answer.extend(TLtBR(position))
    answer.extend(TRtBL(position))
    answer.sort()
    return answer
