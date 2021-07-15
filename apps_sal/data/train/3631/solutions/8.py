def bingo(ticket,win):
    mini_wins = 0
    for arr in ticket:
        mini_wins += any(map(lambda x: ord(x) == arr[1], arr[0]))
    return ['Loser!', 'Winner!'][mini_wins >= win]
