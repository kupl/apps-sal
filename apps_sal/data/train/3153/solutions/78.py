def playerRankUp(pts):
    good = 'Well done! You have advanced to the qualifying stage. Win 2 out of your next 3 games to rank up.'
    if pts >= 100:
        return good
    else:
        return False
