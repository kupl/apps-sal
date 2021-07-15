def did_we_win(plays):
    position = 0
    for play in plays:
        if play[1] == 'run' or play[1] == 'pass':
            position += play[0]
        elif play[1] == 'sack':
            position -= play[0]
        else:
            return False
        if position > 10:
            return True
    return False
