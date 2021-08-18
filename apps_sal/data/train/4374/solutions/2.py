def did_we_win(plays):
    dist = 10
    plays = [t for t in plays if t]
    for play_dist, play in plays:
        if play in ['run', 'pass']:
            dist -= play_dist
            if dist < 0:
                return True
        elif play == 'sack':
            dist += play_dist
        else:
            break
    return False
