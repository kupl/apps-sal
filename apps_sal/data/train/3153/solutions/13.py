def playerRankUp(pts):
    rank_up = 'Well done! You have advanced to the qualifying stage. Win 2 out of your next 3 games to rank up.'
    try:
        rank_up[pts + 4]
    except IndexError:
        return rank_up
    return False
