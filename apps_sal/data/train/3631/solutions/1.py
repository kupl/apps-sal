def bingo(ticket, win):
    return 'Winner!' if sum((w in map(ord, s) for (s, w) in ticket)) >= win else 'Loser!'
