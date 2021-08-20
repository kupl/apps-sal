def bingo(ticket, win):
    counter = 0
    for (x, y) in ticket:
        for i in x:
            counter += 1 if ord(i) == y else 0
    return 'Loser!' if counter < win else 'Winner!'
