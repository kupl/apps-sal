def did_we_win(plays):
    yds = 10
    for play in plays:
        if play[1] == 'turnover':
            return False
        if play[1] == 'sack':
            yds += play[0]
        else:
            yds -= play[0]
        if yds < 0:
            return True
    return False
