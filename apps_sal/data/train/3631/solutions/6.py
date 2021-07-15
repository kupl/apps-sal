def bingo(ticket, win):
    mini_wins = sum(chr(code) in chars for chars, code in ticket)
    return 'Winner!' if mini_wins >= win else 'Loser!'
