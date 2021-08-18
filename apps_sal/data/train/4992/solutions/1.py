def bingo(card, numbers):
    def decode(s): return True if s == 'FREE SPACE' else int(s)
    game = [
        [decode(x) for x in row]
        for row in card[1:]
    ]

    for s in numbers:
        col = 'BINGO'.find(s[0])
        n = int(s[1:])
        for row in range(5):
            val = game[row][col]
            if val is not True and val == n:
                game[row][col] = True
                break

    lines = game
    lines += [[row[col] for row in game] for col in range(5)]
    lines += [[game[i][i] for i in range(5)]]
    lines += [[game[i][4 - i] for i in range(5)]]
    return any(all(x is True for x in line) for line in lines)
