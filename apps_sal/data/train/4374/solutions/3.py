def did_we_win(plays):
    return sum((-100 if p[1][0] == 't' else -p[0] if p[1][0] == 's' else p[0] for p in plays if p)) > 10
