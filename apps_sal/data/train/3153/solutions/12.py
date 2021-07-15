def playerRankUp(pts):
    msg0 = 'Well done! You have advanced to the qualifying stage.'
    msg1 = 'Win 2 out of your next 3 games to rank up.'
    return [False, msg0+' '+msg1][pts > 99]
