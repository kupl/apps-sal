def playerRankUp(pts):

    saying = "Well done! You have advanced to the qualifying stage. Win 2 out of your next 3 games to rank up."
    if pts > 99:
        return saying
    else:
        return False
