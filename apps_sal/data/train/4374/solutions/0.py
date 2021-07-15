def did_we_win(plays):
    plays = [p for p in plays if p]
    return all(p != 'turnover' for y,p in plays) and sum(-y if p == 'sack' else y for y,p in plays) > 10            
