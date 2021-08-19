def bingo(ticket, win):
    winner = sum((1 for (stg, val) in ticket if chr(val) in stg)) >= win
    return 'Winner!' if winner else 'Loser!'
