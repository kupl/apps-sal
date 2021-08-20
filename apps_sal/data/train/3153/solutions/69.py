def playerRankUp(pts, msg='Well done! You have advanced to the qualifying stage. Win 2 out of your next 3 games to rank up.'):
    return False if pts < 99 else msg
