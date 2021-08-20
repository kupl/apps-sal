def bingo(ticket, win):
    won = sum((chr(n) in xs for (xs, n) in ticket)) >= win
    return 'Winner!' if won else 'Loser!'
