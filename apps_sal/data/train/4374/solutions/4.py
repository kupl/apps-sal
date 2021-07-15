def did_we_win(plays):
    if any(play[1] == "turnover" or not play for play in plays if play):
        return False
    if not all(plays):
        return True
    return sum(-yards if action == "sack" else yards for yards, action in plays) > 10

