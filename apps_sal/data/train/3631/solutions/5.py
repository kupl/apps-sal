def bingo(ticket, win):
    return "Loser!" if sum(1 if chr(i[1]) in i[0] else 0 for i in ticket) < win else "Winner!"
