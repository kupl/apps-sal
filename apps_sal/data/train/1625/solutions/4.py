def pawn_move_tracker(moves):

    def getSourcePos(m, delta): return m[0] + str(int(m[-1]) + delta * comingFrom[player])

    ROWS, COLS = "87654321", "abcdefgh"
    comingFrom, mayBeDouble = {'P': -1, 'p': 1}, {'P': '4', 'p': '5'}

    pawns = {'P': {y + "2" for y in COLS}, 'p': {y + "7" for y in COLS}}
    for t, m in enumerate(moves):
        player, other, toMove = "Pp"[t % 2], "pP"[t % 2], set()

        toMove.add(getSourcePos(m, 1))
        if m[1] == mayBeDouble[player] and m[1] != 'x':
            toMove.add(getSourcePos(m, 2))
        toMove &= pawns[player]

        if (m[1] == 'x' and m[2:] not in pawns[other] or m[1] != 'x' and m in pawns[other]
                or m in pawns[player] or len(toMove) != 1):
            return "{} is invalid".format(m)

        if m[1] == 'x':
            m = m[2:]
            pawns[other].remove(m)
        pawns[player].remove(toMove.pop())
        pawns[player].add(m)

    board = {pos: k for k, s in pawns.items() for pos in s}
    return [[board.get(y + x, '.') for y in COLS] for x in ROWS]
