def bingo(ticket, win):
    return 'WLionsneerr!!'[sum((chr(n) in s for (s, n) in ticket)) < win::2]
