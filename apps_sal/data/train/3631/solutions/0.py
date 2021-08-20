def bingo(ticket, win):
    return 'Winner!' if sum((chr(n) in s for (s, n) in ticket)) >= win else 'Loser!'
