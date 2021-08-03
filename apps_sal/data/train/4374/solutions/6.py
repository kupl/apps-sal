def did_we_win(plays):
    yard = 0
    for number, type_play in plays:
        if type_play == "pass":
            win = number
        elif type_play == "run":
            win = number
        elif type_play == "sack":
            win = -number
        elif type_play == "turnover":
            return False
            break
        yard = yard + win
        if yard > 10:
            return True
            break
    if yard > 10:
        return True
    else:
        return False
