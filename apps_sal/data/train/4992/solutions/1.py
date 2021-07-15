def bingo(card, numbers):
    decode = lambda s: True if s == 'FREE SPACE' else int(s)
    game = [
        [decode(x) for x in row]
        for row in card[1:]
    ]

    # Decode each 'number' into a column and number
    for s in numbers:
        col = 'BINGO'.find(s[0])
        n = int(s[1:])
        for row in range(5):
            val = game[row][col]
            if val is not True and val == n:
                # We have that number in the column, mark it as found
                game[row][col] = True
                break

    # Extract all the straight lines through the board
    lines = game                                               # rows 
    lines += [[row[col] for row in game] for col in range(5)]  # cols
    lines += [[game[i][i] for i in range(5)]]                  # leading diagonal
    lines += [[game[i][4-i] for i in range(5)]]                # secondary diagonal
    # See if any lines are all True
    return any(all(x is True for x in line) for line in lines)
